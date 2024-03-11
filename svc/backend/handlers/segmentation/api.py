from flask import Blueprint, request
from src.image import decode


segment = Blueprint('segmentation', __name__, template_folder='segmentation')


@segment.post('/image')
def get_segmented_image():
    image = decode(request.data)
    return '', 200