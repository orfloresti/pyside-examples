from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QPushButton
)
import sys
import random

class Subventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Subventana")
        self.resize(240,120)
        etiqueta = QLabel(f"Soy una subventana... {random.randint(0,100)}")
        layout = QVBoxLayout()
        layout.addWidget(etiqueta)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal")
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        boton_mostrar = QPushButton("Mostrar subventana")
        boton_mostrar.clicked.connect(self.mostrar_subventana)
        layout.addWidget(boton_mostrar)
        self.subventana = None

        boton_ocultar = QPushButton("Ocultar subventana")
        boton_ocultar.clicked.connect(self.ocultar_subventana)
        layout.addWidget(boton_ocultar)
    
    def ocultar_subventana(self):
        if self.subventana and self.subventana.isVisible():
            self.subventana.hide()

    def mostrar_subventana(self):
        if not self.subventana:
            self.subventana = Subventana()
        self.subventana.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())