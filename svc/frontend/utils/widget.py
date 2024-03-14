from typing import Iterable
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QMainWindow,
    QToolBar
)
from PyQt6.QtGui import QAction


def add_toolbar(parent: QMainWindow, items: Iterable, 
                area: Qt.ToolBarArea = Qt.ToolBarArea.TopToolBarArea) -> QToolBar:
    '''
        This function encapsulates logic of adding toolbar to the window.
    '''
    toolbar = QToolBar(parent)
    for item in items:
        if issubclass(type(item), QAction):
            toolbar.addAction(item)
        elif issubclass(type(item), QWidget):
            toolbar.addWidget(item)
    parent.addToolBar(area, toolbar)
    return toolbar