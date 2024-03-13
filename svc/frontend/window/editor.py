from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow
)
from PyQt6.QtGui import (
    QImage,
    QAction
)
from ..utils.widget import add_toolbar


class EditorWindow(QMainWindow):
    def __init__(self, initial_segmentation: QImage) -> None:
        super(EditorWindow, self).__init__()
        self.segmentation_image = initial_segmentation
        self._setup_layout()
        self.setWindowTitle('Segmentation Editor')

    def _setup_layout(self) -> None:
        add_toolbar(parent=self, actions=[
            QAction('Save'),
            QAction('Reset')
        ])
        add_toolbar(parent=self, actions=[], area=Qt.ToolBarArea.LeftToolBarArea)