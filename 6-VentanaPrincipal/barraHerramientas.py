from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QStatusBar,
    QToolBar, 
    QLabel,
    QDockWidget)
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt
from pathlib import Path
import sys

def absPath(file):
    return str(Path(__file__).parent.absolute()/file)

class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480,320)
        icono = QIcon(absPath("save.png"))
        self.setWindowIcon(icono)
        self.setStatusBar(QStatusBar(self))
        self.construir_menu()
        self.construir_herramientas()

        self.construir_docks()

        self.setCentralWidget(Caja("gray"))
    
    def construir_docks(self):
        dock1 = QDockWidget()
        dock1.setWindowTitle("Dock")
        dock1.setWidget(Caja("green"))
        #dock1.setMinimumHeight(100)
        #dock1.setMinimumWidth(150)
        dock1.setMinimumSize(150, 100)
        dock1.setFeatures(QDockWidget.NoDockWidgetFeatures | 
                        QDockWidget.DockWidgetFloatable |
                        QDockWidget.DockWidgetClosable |
                        QDockWidget.DockWidgetMovable)

        self.addDockWidget(Qt.LeftDockWidgetArea, dock1)

        dock2 = QDockWidget()
        dock2.setWindowTitle("Dock")
        dock2.setWidget(Caja("yellow"))
        dock2.setMinimumSize(150, 100)
        self.addDockWidget(Qt.RightDockWidgetArea, dock2)

        dock3 = QDockWidget()
        dock3.setWindowTitle("Dock")
        dock3.setWidget(Caja("Blue"))
        dock3.setMinimumSize(150, 100)
        self.addDockWidget(Qt.BottomDockWidgetArea, dock3)

    def construir_herramientas(self):
        herramientas = QToolBar("Barra de herramientas")
        herramientas.addAction(QIcon(absPath("exit.png")),
            "S&alir",
            self.close)
        herramientas.addAction(self.action_info)
        self.addToolBar(herramientas)

    def construir_menu(self):
        menu = self.menuBar()

        menu_archivo = menu.addMenu("&Menú")
        menu_archivo.addAction("&Prueba")

        submenu_archivo = menu_archivo.addMenu("&Submenu")
        submenu_archivo.addAction("Subopción &1")
        submenu_archivo.addAction("Subopción &2")

        menu_archivo.addSeparator()
        menu_archivo.addAction(QIcon(absPath("exit.png")),
            "S&alir",
            self.close,
            "Ctrl+Q")

        menu_ayuda = menu.addMenu("Ay&uda")
        accion_info = QAction("&Información", self)
        accion_info.setIcon(QIcon(absPath("info.png")))
        accion_info.setShortcut("Ctrl+I")
        accion_info.triggered.connect(self.mostrar_info)
        accion_info.setStatusTip("Muestra información irrelevante")
        menu_ayuda.addAction(accion_info)
        self.action_info = accion_info

    def mostrar_info(self):
        QMessageBox.about(self, "Información", "Esto es un texto informativo")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())