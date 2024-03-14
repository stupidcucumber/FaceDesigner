from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel
)
from PyQt6.QtGui import (
    QPixmap,
    QAction
)
from ..utils.widget import add_toolbar


class EditorWindow(QMainWindow):
    def __init__(self, canvas: QPixmap) -> None:
        super(EditorWindow, self).__init__()
        self.segmentation_image_canvas = canvas
        self._setup_layout()
        self.setWindowTitle('Segmentation Editor')

    def _setup_canvas(self, canvas: QPixmap) -> None:
        label = QLabel(self)
        label.setPixmap(canvas)
        self.setCentralWidget(label)

    def _setup_layout(self) -> None:
        add_toolbar(parent=self, actions=[
            QAction('Save', self),
            QAction('Reset', self)
        ])
        add_toolbar(parent=self, actions=[], area=Qt.ToolBarArea.LeftToolBarArea)
        self._setup_canvas(canvas=self.segmentation_image_canvas)
