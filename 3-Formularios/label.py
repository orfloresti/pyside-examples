import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt
from pathlib import Path

def absPath(file):
    return str(Path(__file__).parent.absolute()/file)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola Mundo")
        self.resize(480,320)

        etiqueta = QLabel("Soy una etiqueta")
        # fuente = etiqueta.font()
        # fuente.setPointSize(24)
        fuente = QFont("Noto Mono", 24)
        etiqueta.setFont(fuente)
        etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        imagen = QPixmap(absPath("imagen.jpg"))
        etiqueta.setPixmap(imagen)
        etiqueta.setScaledContents(True)

        self.setCentralWidget(etiqueta)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
