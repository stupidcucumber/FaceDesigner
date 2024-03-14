from typing import Callable
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QSlider,
    QLabel,
    QFileDialog
)
from PyQt6.QtGui import (
    QPixmap,
    QAction
)
from ..utils.widget import add_toolbar
from ..widgets import Canvas, ColorButton


class EditorWindow(QMainWindow):
    def __init__(self, image_label: QLabel | None = None, color_mapping: dict = None) -> None:
        super(EditorWindow, self).__init__()
        self.image_label = image_label
        self.original_pixmap = image_label.pixmap()
        self.canvas = Canvas(initial_pixmap=image_label.pixmap(), size=QSize(640, 640))
        self.color_mapping = color_mapping
        self._setup_layout()
        self.setWindowTitle('Segmentation Editor')

    def _setup_slider(self) -> QSlider:
        slider = QSlider(Qt.Orientation.Vertical, self)
        slider.setMaximumHeight(128)
        slider.setTickInterval(12)
        slider.setSingleStep(12)
        slider.setTickPosition(QSlider.TickPosition.TicksRight)
        slider.valueChanged.connect(lambda event: self.canvas.set_pen_width(slider.value()))
        return slider
    
    def _setup_color_buttons(self) -> list[QPushButton]:
        buttons = []
        for color in self.color_mapping.values():
            button = ColorButton(color=color)
            button.pressed.connect(lambda color=color: self.canvas.set_pen_color(color=color))
            buttons.append(button)
        return buttons

    def _setup_painting_tools(self) -> list[QPushButton]:
        widgets = [
            self._setup_slider(),
            *self._setup_color_buttons()
        ]
        return widgets
    
    def _setup_action(self, title: str, slot: Callable) -> QAction:
        action = QAction(title, self)
        action.triggered.connect(slot)
        return action
    
    def _save(self):
        original_size = self.image_label.pixmap().size()
        edited_pixmap = self.canvas.pixmap().scaled(original_size,
                                                    Qt.AspectRatioMode.KeepAspectRatio, 
                                                    Qt.TransformationMode.FastTransformation)
        self.image_label.setPixmap(edited_pixmap)
        self.close()

    def _export(self):
        path = QFileDialog.getSaveFileName(self,
                                          caption='Save altered segmentation map.',
                                          directory='.')[0]
        original_size = self.image_label.pixmap().size()
        edited_pixmap = self.canvas.pixmap().scaled(original_size,
                                                    Qt.AspectRatioMode.KeepAspectRatio, 
                                                    Qt.TransformationMode.FastTransformation)
        edited_pixmap.save(path + '.png', format='png')


    def _setup_layout(self) -> None:
        add_toolbar(parent=self, items=[
            self._setup_action(title='Save', slot=lambda event: self._save()),
            self._setup_action(title='Export', slot=lambda event: self._export()),
            self._setup_action(title='Reset', slot=lambda event: self.canvas.setPixmap(self.original_pixmap))
        ])
        add_toolbar(parent=self, items=self._setup_painting_tools(), 
                                 area=Qt.ToolBarArea.LeftToolBarArea)
        self.setCentralWidget(self.canvas)
