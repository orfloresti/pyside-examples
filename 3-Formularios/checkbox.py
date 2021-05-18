import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola Mundo")
        self.resize(480,320)

        casilla = QCheckBox("Casilla de verificación")
        casilla.setCheckState(Qt.PartiallyChecked)
        casilla.stateChanged.connect(self.estado_cambiado)
        # casilla.setEnabled(False)

        print("Activada?", casilla.isChecked())
        print("Parcial?", casilla.isTristate())

        self.setCentralWidget(casilla)

    def estado_cambiado(self, estado):
        if(estado == Qt.Checked):
            print("Cassilla marcada")
        if(estado == Qt.Unchecked):
            print("Cassilla desmarcada")
        if(estado == Qt.PartiallyChecked):
            print("Cassilla parcial")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
