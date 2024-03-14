from PyQt6.QtWidgets import (
    QPushButton
)


class ColorButton(QPushButton):
    def __init__(self, color: list[int]) -> None:
        super(ColorButton, self).__init__()
        self.color = color
        self.setFixedSize(24, 24)
        self.setStyleSheet('background-color: rgb(%d, %d, %d);' % tuple(color))