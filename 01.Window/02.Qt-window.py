# Create a simple window with Python and Qt6
import sys
from PyQt6.QtWidgets import QMainWindow as QMainW
from PyQt6.QtWidgets import QApplication as QApp

class MainWindow(QMainW):
    def __init__(self, *args, **kwargs):
      super(MainWindow, self).__init__(*args, **kwargs)

      # Adding status bar 
      self.statusbar = self.statusBar()      
      self.statusbar.showMessage("Ready")

      self.show()

app = QApp(sys.argv)

# Adding application and Organization name
app.setApplicationName("Hello World!")
app.setOrganizationName("ACME")

window = MainWindow()

app.exec()