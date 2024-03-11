import requests
import pathlib
import cv2
from .utils import decode_image, encode_image


def get_segmentation(image_path: pathlib.Path, color_mapping: dict, url: str) -> cv2.Mat:
    image = cv2.imread(str(image_path))
    initial_height, initial_width, _ = image.shape
    response = requests.post(url=url,
                            json={
                                'ColorMapping': color_mapping,
                                'Image': encode_image(image=image)
                            })
    segmentation = decode_image(response.json()['Segmentation'])
    segmentation = cv2.resize(segmentation, dsize=(initial_width, initial_height))
    return segmentation