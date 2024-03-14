import sys
from svc.frontend.window import MainWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPixmap

app = QApplication(sys.argv)
pixmap = QPixmap('misc/segmentation/input.png')
main_window = MainWindow()
main_window.show()
app.exec() 