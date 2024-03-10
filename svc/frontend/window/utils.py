import pathlib
import cv2


def load_image(path: pathlib.Path, size: tuple=(512, 512)) -> cv2.Mat:
    image = cv2.imread(filename=str(path))
    image = cv2.resize(image, dsize=size)
    return image