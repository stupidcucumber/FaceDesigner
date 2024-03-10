import sys
from svc.frontend.window import MainWindow
from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec() 