import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget

# IMPORTAR TODAS LAS PANTALLAS
from Bienvenida import Ui_Bienvenida
from Pantalla_De_Inicio import Ui_Pantalla_De_Inicio
from Lección_1 import Ui_Lección_1
from Lección_2 import Ui_Lección_2
from Lección_3 import Ui_Form as Ui_Lección_3
from Lección_4 import Ui_Form as Ui_Lección_4
from Lección_5 import Ui_MainWindow as Ui_Lección_5
from Lección_6 import Ui_MainWindow as Ui_Lección_6
from Lección_7 import Ui_MainWindow as Ui_Lección_7
from Lección_8 import Ui_MainWindow as Ui_Lección_8

from Quiz_P1 import Ui_MainWindow as Ui_Quiz_P1
from Quiz_P2 import Ui_MainWindow as Ui_Quiz_P2
from Quiz_P3 import Ui_MainWindow as Ui_Quiz_P3
from Quiz_P4 import Ui_MainWindow as Ui_Quiz_P4
from Quiz_P5 import Ui_MainWindow as Ui_Quiz_P5


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Curso Básico de Git")
        self.resize(900, 650)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Crear pantallas
        self.bienvenida = self.crear_pantalla(Ui_Bienvenida)
        self.inicio = self.crear_pantalla(Ui_Pantalla_De_Inicio)
        self.l1 = self.crear_pantalla(Ui_Leccion1)
        self.l2 = self.crear_pantalla(Ui_Leccion2)
        self.l3 = self.crear_pantalla(Ui_Leccion3)
        self.l4 = self.crear_pantalla(Ui_Leccion4)
        self.l5 = self.crear_pantalla(Ui_Leccion5)
        self.l6 = self.crear_pantalla(Ui_Leccion6)
        self.l7 = self.crear_pantalla(Ui_Leccion7)
        self.l8 = self.crear_pantalla(Ui_Leccion8)

        self.q1 = self.crear_pantalla(Ui_Quiz1)
        self.q2 = self.crear_pantalla(Ui_Quiz2)
        self.q3 = self.crear_pantalla(Ui_Quiz3)
        self.q4 = self.crear_pantalla(Ui_Quiz4)
        self.q5 = self.crear_pantalla(Ui_Quiz5)

        # Conexiones de botones
        self.bienvenida.pushButton.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.inicio)
        )

        self.inicio.pushButton.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.l1)
        )

        self.l1.pushButton.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.l2)
        )

        self.l2.pushButton.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.l3)
        )

        self.l3.pushButton.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.l4)
        )

        self.l4.pushButton.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.l5)
        )

        self.l5.pushButton_2.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.l6)
        )

        self.l6.pushButton.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.l7)
        )

        self.l7.pushButton_2.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.l8)
        )

        self.l8.pushButton_2.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.q1)
        )

        self.q1.pushButton_2.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.q2)
        )

        self.q2.pushButton_6.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.q3)
        )

        self.q3.pushButton_6.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.q4)
        )

        self.q4.pushButton_2.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.q5)
        )

    def crear_pantalla(self, UiClase):
        widget = QWidget()
        ui = UiClase()
        ui.setupUi(widget)
        widget.ui = ui
        self.stack.addWidget(widget)
        return ui


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
