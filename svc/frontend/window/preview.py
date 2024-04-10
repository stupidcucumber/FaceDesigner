from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QWidget,
    QVBoxLayout
)
from PyQt6.QtGui import (
    QImage,
    QPixmap
)


class PreviewWindow(QMainWindow):
    def __init__(self, qimage: QImage) -> None:
        super(PreviewWindow, self).__init__()
        self.pixmap = QPixmap(qimage)
        self._set_layout()

    def _set_layout(self) -> None:
        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)
        self.setCentralWidget(self.label)