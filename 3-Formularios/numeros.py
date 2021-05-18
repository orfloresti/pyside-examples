import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox
from PySide6.QtWidgets import QApplication, QMainWindow, QDoubleSpinBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola Mundo")

        numero = QDoubleSpinBox()
        numero.setRange(0, 20)
        numero.setSingleStep(0.5)
        numero.setPrefix("$ ")
        numero.setSuffix(" %")
        numero.setValue(8)

        print(numero.value())

        numero.valueChanged.connect(self.valor_cambiado)
        self.setCentralWidget(numero)

    def valor_cambiado(self, numero):
        print("Valor cambiado", numero)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())