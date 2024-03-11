import base64
import numpy as np
import cv2


def decode(image: str) -> cv2.Mat:
    image_bytes = base64.b64decode(image)
    image_arr = np.fromstring(image_bytes, np.uint8)
    image = cv2.imdecode(image_arr, cv2.IMREAD_COLOR)
    return image