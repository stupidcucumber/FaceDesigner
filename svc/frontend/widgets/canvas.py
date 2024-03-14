from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import (
    QMouseEvent,
    QPixmap,
    QPainter
)


class Canvas(QLabel):
    def __init__(self, initial_pixmap: QPixmap | None = None) -> None:
        super(Canvas, self).__init__()
        if initial_pixmap:
            self.setPixmap(initial_pixmap)
        else:
            pixmap = QPixmap(512, 512)
            pixmap.fill(Qt.GlobalColor.white)
            self.setPixmap(pixmap)
        self.last_point = None

    def mouseMoveEvent(self, event: QMouseEvent | None) -> None:
        if not self.last_point:
            self.last_point = event.pos()
            return
        pixmap = self.pixmap()
        painter = QPainter(pixmap)
        painter.drawLine(self.last_point, event.pos())
        painter.end()
        self.setPixmap(pixmap)
        self.last_point = event.pos()

    def mouseReleaseEvent(self, event: QMouseEvent | None) -> None:
        self.last_point = None

    