from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtGui import QIcon
from pathlib import Path
import sys

def absPath(file):
    return str(Path(__file__).parent.absolute()/file)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480,320)
        icono = QIcon(absPath("save.png"))
        self.setWindowIcon(icono)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())