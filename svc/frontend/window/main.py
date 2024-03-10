from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget


class MainWindow(QMainWindow):
    def __init__(self, title: str='FaceDesigner 🔥') -> None:
        super(MainWindow, self).__init__()

        self.setWindowTitle(title)