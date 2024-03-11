import base64, pathlib, json
import numpy as np
import cv2


def load_color_mapping(path: pathlib.Path) -> dict:
    with path.open() as cmap:
        result = json.load(cmap)
    return result


def decode_image(image: str) -> cv2.Mat:
    image_bytes = base64.b64decode(image)
    image_arr = np.fromstring(image_bytes, np.uint8)
    image = cv2.imdecode(image_arr, cv2.IMREAD_COLOR)
    return image


def encode_image(image: cv2.Mat) -> str:
    return base64.b64encode(cv2.imencode('.jpg', image)[1]).decode()