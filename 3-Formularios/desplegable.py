import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola Mundo")
        self.resize(480,320)
        
        desplegable = QComboBox()
        desplegable.addItems(["", "Opción 1", "Opción 2", "Opción 3"])
        desplegable.currentIndexChanged.connect(self.indice_cambiado)
        desplegable.currentTextChanged.connect(self.texto_cambiado)

        print("Índice actual", desplegable.currentIndex())
        print("Texto actual", desplegable.currentText())

        self.setCentralWidget(desplegable)

    def indice_cambiado(self, indice):
        print("Nuevo indice", indice)

    def texto_cambiado(self, texto):
        print("Nuevo texto", texto)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
