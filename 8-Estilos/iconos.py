from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QStyle
)

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        icono = self.style().standardIcon(QStyle.SP_DialogSaveButton)
        boton = QPushButton(icono, "Boton guardar")
        self.setCentralWidget(boton)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())