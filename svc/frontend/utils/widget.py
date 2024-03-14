from typing import Iterable
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QToolBar
)


def add_toolbar(parent: QMainWindow, actions: Iterable, 
                area: Qt.ToolBarArea = Qt.ToolBarArea.TopToolBarArea) -> QToolBar:
    '''
        This function encapsulates logic of adding toolbar to the window.
    '''
    toolbar = QToolBar(parent)
    toolbar.addActions(actions)
    parent.addToolBar(area, toolbar)
    return toolbar