from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import (
    QMouseEvent,
    QPixmap,
    QPainter,
    QPen,
    QColor
)


class Canvas(QLabel):
    def __init__(self, initial_pixmap: QPixmap | None = None, size: QSize | None = QSize(512, 512)) -> None:
        super(Canvas, self).__init__()
        if initial_pixmap:
            self.setPixmap(initial_pixmap.scaled(size, 
                                                 Qt.AspectRatioMode.KeepAspectRatio, 
                                                 Qt.TransformationMode.FastTransformation))
            self.resize(size)
        else:
            pixmap = QPixmap(size)
            pixmap.fill(Qt.GlobalColor.white)
            self.setPixmap(pixmap)
        self.last_point = None
        self.pen = QPen()

    def set_pen_width(self, size: int) -> None:
        self.pen.setWidth(size)

    def set_pen_color(self, color: list) -> None:
        self.pen.setColor(QColor(*color))

    def mouseMoveEvent(self, event: QMouseEvent | None) -> None:
        if not self.last_point:
            self.last_point = event.pos()
            return
        pixmap = self.pixmap()
        painter = QPainter(pixmap)
        painter.setPen(self.pen)
        painter.drawLine(self.last_point, event.pos())
        painter.end()
        self.setPixmap(pixmap)
        self.last_point = event.pos()

    def mouseReleaseEvent(self, event: QMouseEvent | None) -> None:
        self.last_point = None

    