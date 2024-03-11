import cv2, base64
from flask import Blueprint, request
from src.image import decode
from src.segmentation import SegmentationModel


segment = Blueprint('segmentation', __name__, template_folder='segmentation')
model = SegmentationModel(weights='weights/segmentation/best_weights.pt', device='cpu')

@segment.post('/image')
def get_segmented_image():
    image = decode(request.json['Image'])
    segmentation = model.segment(image=image, cmap=request.json['ColorMapping'])
    string = base64.b64encode(cv2.imencode('.jpg', segmentation)[1]).decode()
    return {'Segmentation': string}, 200