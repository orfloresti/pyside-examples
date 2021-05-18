import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola Mundo")
        self.resize(480,320)

        lista = QListWidget()
        lista.addItems(["Opción 1", "Opción 2", "Opción 3"])
        lista.currentItemChanged.connect(self.item_cambiado)

        print(lista.currentItem())

        self.setCentralWidget(lista)
    
    def item_cambiado(self, item):
        print("Nuevo item", item.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

