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
from typing import Callable
import pathlib
from ..utils.request import get_segmentation
from ..settings.utils import load_color_mapping
from ..utils.image import cv2qimage, instantiate_qimage, instantiate_label_image
from .editor import EditorWindow


class MainWindow(QMainWindow):
    def __init__(self, title: str='FaceDesigner 🔥') -> None:
        super(MainWindow, self).__init__()
        self.nopicture_path = pathlib.Path('svc', 'frontend', 'icons', 'nopicture.jpg')
        self.setWindowTitle(title)
        self._add_toolbar()
        self.images = self._add_layout()
        self.editor_window = None
        self.is_segmentation_generated = False
        self.current_image_path = self.nopicture_path

    def open_editor(self, event) -> None:
        self.editor_window = EditorWindow(pixmap=self.images['segmentation'].pixmap())
        self.editor_window.show()

    def _load_image(self, event) -> None:
        path = QFileDialog.getOpenFileName(
            self,
            caption='Open image',
            directory='.'
        )[0]
        self.current_image_path = path
        if path != '':
            self.images['image'].setPixmap(QPixmap(
                instantiate_qimage(path=path, dsize=(512, 512))
            ))
            self.images['segmentation'].setPixmap(QPixmap(
                instantiate_qimage(path=self.nopicture_path, dsize=(512, 512))
            ))
            self.is_segmentation_generated = False

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
    
    def _instantiate_widget(self, parent, layout, widgets: list[QWidget]) -> QWidget:
        for widget in widgets:
            layout.addWidget(widget)
        main_widget = QWidget(parent)
        main_widget.setLayout(layout)
        return main_widget
    
    def _create_push_button(self, text: str, slot: Callable) -> QPushButton:
        button = QPushButton(text, self)
        button.clicked.connect(slot=slot)
        return button
    
    def _update_segmentation(self, event) -> None:
        if not self.is_segmentation_generated:
            segmentation_image = get_segmentation(
                            image_path=self.current_image_path,
                            color_mapping=load_color_mapping(path=pathlib.Path('svc', 'frontend', 'settings', 'color_mapping.json')),
                            url='http://localhost:5050/segmentation/image')
            self.images['segmentation'].setPixmap(QPixmap(cv2qimage(segmentation_image, dsize=(512, 512))))
            self.is_segmentation_generated = True

    def _add_layout(self) -> dict[QLabel]:
        result = dict()
        result['image'] = instantiate_label_image(path=self.nopicture_path, parent=self,
                                                  dsize=(512, 512))
        result['segmentation'] = instantiate_label_image(path=self.nopicture_path, parent=self,
                                                         dsize=(512, 512))
        image_widget_0 = self._instantiate_widget(
            parent=self,
            layout=QVBoxLayout(),
            widgets=[
                QLabel('Image:', self),
                result['image']
            ]
        )
        image_widget_1 = self._instantiate_widget(
            parent=self,
            layout=QVBoxLayout(),
            widgets=[
                QLabel('Segmentation:', self),
                result['segmentation']
            ]
        )
        images = self._instantiate_widget(self, QHBoxLayout(), [image_widget_0, image_widget_1])
        central_widget = self._instantiate_widget(self, QVBoxLayout(), 
                                                  [
                                                      images,
                                                      self._create_push_button('Generate Segmentation Map', slot=self._update_segmentation),
                                                      self._create_push_button('Edit Segmentation Map', slot=self.open_editor)
                                                ])
        self.setCentralWidget(central_widget)
        return result