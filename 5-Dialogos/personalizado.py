from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)
        boton = QPushButton("Mostrar diálogo")
        boton.clicked.connect(self.boton_clicado)
        self.setCentralWidget(boton)
    
    def boton_clicado(self):
        print("Hola")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
