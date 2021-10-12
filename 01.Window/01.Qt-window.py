# Create a simple window with Python and Qt5 
import sys
from PyQt6.QtWidgets import QMainWindow as QMainW, QApplication as QApp

class MainWindow(QMainW):
    def __init__(self, *args, **kwargs):
      super(MainWindow, self).__init__(*args, **kwargs)
      self.show()

app = QApp(sys.argv)
window = MainWindow()

app.exec()