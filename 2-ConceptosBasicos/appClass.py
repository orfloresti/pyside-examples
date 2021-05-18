import sys
# from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Hola mundo")
boton = QPushButton("Soy un botón")
window.setCentralWidget(boton)

window.show()
sys.exit(app.exec_())
