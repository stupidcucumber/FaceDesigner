import torch
from torchvision import transforms
import pathlib
import numpy as np
import cv2


class SegmentationModel():
    def __init__(self, weights: pathlib.Path, device: str) -> None:
        self.model = self._load_model(weights=weights, device=device)
        self.transform = transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406],
                    std=[0.229, 0.224, 0.225]
                ),
                transforms.Resize(size=(512, 512))
            ]
        )

    def _load_model(self, weights: pathlib.Path, device: str):
        model = torch.load(weights, map_location=lambda loc, state: loc)
        model.to(device)
        return model
    
    def _load_input(self, image: cv2.Mat):
        input = self.transform(image)
        return torch.unsqueeze(input, dim=0)
    
    def _decode_output(self, logits: torch.Tensor, dim: int = 0) -> torch.Tensor:
        indeces = torch.argmax(logits, dim=dim, keepdim=True)
        result = torch.zeros_like(logits, dtype=torch.uint8)
        return result.scatter(dim=dim, index=indeces, value=1)
    
    def _construct_image(self, output: torch.Tensor, cmap: dict) -> np.ndarray:
        output_shape = (*output.shape[1:], 3)
        image = np.zeros(shape=output_shape)
        decoded_output = self._decode_output(logits=output)
        for layer_index in cmap.keys():
            index = int(layer_index)
            _raw_layer = np.stack([decoded_output[index], decoded_output[index], decoded_output[index]]).transpose(1, 2, 0)
            layer = _raw_layer * np.full(shape=output_shape, 
                                        fill_value=cmap[layer_index])
            image = image + layer
        return image

    def segment(self, image: cv2.Mat, cmap: dict) -> np.ndarray:
        '''
            Segmenting Image of shape [1, 3, 512, 512]
        '''
        input = self._load_input(image=image)
        output = self.model(input)
        image = self._construct_image(output=output['out'][0], cmap=cmap)
        return image
