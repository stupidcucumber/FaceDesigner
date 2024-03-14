from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow
)
from PyQt6.QtGui import (
    QPixmap,
    QAction
)
from ..utils.widget import add_toolbar
from ..widgets import Canvas

class EditorWindow(QMainWindow):
    def __init__(self, pixmap: QPixmap | None = None) -> None:
        super(EditorWindow, self).__init__()
        self.canvas = Canvas(initial_pixmap=pixmap)
        self._setup_layout()
        self.setWindowTitle('Segmentation Editor')

    def _setup_layout(self) -> None:
        add_toolbar(parent=self, actions=[
            QAction('Save', self),
            QAction('Reset', self)
        ])
        add_toolbar(parent=self, actions=[], area=Qt.ToolBarArea.LeftToolBarArea)
        self.setCentralWidget(self.canvas)
