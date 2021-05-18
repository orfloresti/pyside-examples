from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox
from PySide6.QtGui import QIcon
from pathlib import Path
import sys

def absPath(file):
    return str(Path(__file__).parent.absolute() / file)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)
        self.setWindowIcon(QIcon(absPath("save.png")))

        boton = QPushButton("Mostrar diálogo")
        boton.clicked.connect(self.boton_clicado)
        self.setCentralWidget(boton)
    
    def boton_clicado(self):
        # dialogo = QMessageBox.question(self, "Cuestión", "Esto es una pregunta")
        # dialogo = QMessageBox.about(self, "Acerca de", "Esto es un dialogo de acerca de")
        # dialogo = QMessageBox.critical(self, "Error", "Esto es un mensaje crítico")
        # dialogo = QMessageBox.information(self, "Information", "Information")
        dialogo = QMessageBox.warning(
            self, "Advertencia", "¿Seguro que deseas hacer algo?",
            buttons=QMessageBox.Apply | QMessageBox.Cancel)

        # if dialogo == QMessageBox.Yes:
        #     print("Ha respondido si")
        # else: 
        #     print("Ha respondido no")

        if dialogo == QMessageBox.Apply:
            print("Aplicamos los cambios")
        else:
            print("Cancel")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
