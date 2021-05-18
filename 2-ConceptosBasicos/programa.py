import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola Mundo")
        self.resize(480,320)

        boton = QPushButton("Soy un botón")

        boton.setCheckable(True)
        boton.clicked.connect(self.boton_alternado)

        self.setCentralWidget(boton)
        self.boton = boton

    def boton_alternado(self, valor):
        if valor:
            self.boton.setText("Estoy activado")
        else:
            self.boton.setText("Estoy desactivado")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
