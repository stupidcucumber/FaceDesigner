import base64, pathlib
import numpy as np
import cv2
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QLabel


def decode_image(image: str) -> cv2.Mat:
    image_bytes = base64.b64decode(image)
    image_arr = np.fromstring(image_bytes, np.uint8)
    image = cv2.imdecode(image_arr, cv2.IMREAD_COLOR)
    return image

def encode_image(image: cv2.Mat) -> str:
    return base64.b64encode(cv2.imencode('.jpg', image)[1]).decode()

def cv2qimage(image: cv2.Mat, dsize: tuple | None = None) -> QImage:
    if dsize:
        image = cv2.resize(image, dsize=dsize)
    height, width, _ = image.shape
    return QImage(image.data, width, height, 3 * width, QImage.Format.Format_RGB888).rgbSwapped()

def instantiate_qimage(path: str | pathlib.Path, dsize: tuple | None = None) -> QImage:
    image = cv2.imread(str(path))
    return cv2qimage(image=image, dsize=dsize)

def instantiate_label_image(path: str | pathlib.Path, parent, dsize: tuple | None = None) -> QLabel:
    label = QLabel(parent)
    label.setPixmap(QPixmap(instantiate_qimage(path=path, dsize=dsize)))
    return label
