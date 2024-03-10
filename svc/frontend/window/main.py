from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, 
    QToolBar
)
from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self, title: str='FaceDesigner 🔥') -> None:
        super(MainWindow, self).__init__()
        self.setWindowTitle(title)
        self._add_toolbar()

    def _add_toolbar(self) -> None:
        toolbar = QToolBar('main-toolbar')
        open_button = QAction('Open', toolbar)
        save_button = QAction('Save', toolbar)
        toolbar.addActions(
            [open_button, save_button]
        )
        self.addToolBar(toolbar)