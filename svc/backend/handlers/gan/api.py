import cv2, base64
from flask import Blueprint, request
from src.image import decode
from src.segmentation import SegmentationModel


gan = Blueprint('gan', __name__, template_folder='gan')
model = SegmentationModel(weights='weights/segmentation/best_weights.pt', device='cpu')

@gan.post('/image')
def get_generated_image():
    image = decode(request.json['Image'])
    new_segmentation_image = decode(request.json['NewSegmentationImage'])
    old_segmentation_image = decode(request.json['OldSegmentationImage'])
    segmentation = model.segment(image=image, cmap=request.json['ColorMapping'])
    string = base64.b64encode(cv2.imencode('.jpg', segmentation)[1]).decode()
    return {'generatedImage': string}, 200