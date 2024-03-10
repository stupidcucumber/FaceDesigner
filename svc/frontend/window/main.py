from PyQt6.QtWidgets import (
    QMainWindow, 
    QToolBar,
    QFileDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QWidget,
    QPushButton
)
from PyQt6.QtGui import QAction, QPixmap
import pathlib
from PIL import Image
from .utils import load_image


class MainWindow(QMainWindow):
    def __init__(self, title: str='FaceDesigner 🔥') -> None:
        super(MainWindow, self).__init__()
        self.setWindowTitle(title)
        self._add_toolbar()
        self.images = self._add_layout()

    def _load_image(self, event) -> None:
        path = QFileDialog.getOpenFileName(
            self,
            caption='Open image',
            directory='.'
        )[0]
        if path != '':
            self.images['image'].setPixmap(QPixmap(path))

    def _create_open_button(self, toolbar: QToolBar) -> QAction:
        button = QAction('Open', toolbar)
        button.triggered.connect(self._load_image)
        return button

    def _add_toolbar(self) -> None:
        toolbar = QToolBar('main-toolbar')
        save_button = QAction('Save', toolbar)
        toolbar.addActions(
            [
                self._create_open_button(toolbar=toolbar), 
                save_button
            ]
        )
        self.addToolBar(toolbar)

    def _instantiate_image_widget(self, parent, layout, label: str, image_path: str) -> QWidget:
        title = QLabel(label, parent)
        image = QLabel(parent)
        image.setPixmap(QPixmap(image_path))
        layout.addWidget(title)
        layout.addWidget(image)
        widget = QWidget(parent)
        widget.setLayout(layout)
        return widget, image
    
    def _instantiate_widget(self, parent, layout, widgets: list[QWidget]) -> QWidget:
        for widget in widgets:
            layout.addWidget(widget)
        main_widget = QWidget(parent)
        main_widget.setLayout(layout)
        return main_widget

    def _add_layout(self) -> dict[QLabel]:
        nopicture_path = pathlib.Path('svc', 'frontend', 'icons', 'nopicture.jpg')
        result = dict()
        image_widget_0, image = self._instantiate_image_widget(self, QVBoxLayout(), label='Image:',
                                                        image_path=str(nopicture_path))
        image_widget_1, segmentation = self._instantiate_image_widget(self, QVBoxLayout(), label='Segmentation:',
                                                        image_path=str(nopicture_path))
        images = self._instantiate_widget(self, QHBoxLayout(), [image_widget_0, image_widget_1])
        central_widget = self._instantiate_widget(self, QVBoxLayout(), 
                                                  [
                                                      images,
                                                      QPushButton('Edit Segmentation Map', self),
                                                      QPushButton('Generate', self)
                                                ])
        self.setCentralWidget(central_widget)
        result['image'] = image
        result['segmentation'] = segmentation
        return result