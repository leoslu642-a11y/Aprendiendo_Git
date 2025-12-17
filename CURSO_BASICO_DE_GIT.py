import sys
import os
from PyQt5 import QtWidgets

# --- Configuración de Ruta para la carpeta Pantallas ---
# Esto le dice a Python que busque los archivos dentro de 'Pantallas'
sys.path.append(os.path.join(os.path.dirname(__file__), 'Pantallas'))

# --- Importación de tus clases de Interfaz ---
try:
    from Bienvenida import Ui_Bienvenida
    from Pantalla_De_Inicio import Ui_Pantalla_De_Inicio
    from Sección_2 import Ui_MainWindow as Ui_Seccion2
    from Lección_1 import Ui_Leccion1
    from Lección_2 import Ui_Leccion2
    from Lección_3 import Ui_Form as Ui_Leccion3
    from Lección_4 import Ui_Form as Ui_Leccion4
    from Lección_5 import Ui_MainWindow as Ui_Leccion5
    from Lección_6 import Ui_MainWindow as Ui_Leccion6
    from Lección_7 import Ui_MainWindow as Ui_Leccion7
    from Lección_8_quiz import Ui_MainWindow as Ui_Leccion8
    from Quiz_P1 import Ui_MainWindow as Ui_Q1
    from Quiz_P2 import Ui_MainWindow as Ui_Q2
    from Quiz_P3 import Ui_MainWindow as Ui_Q3
    from Quiz_P4 import Ui_MainWindow as Ui_Q4
    from Quiz_P5 import Ui_MainWindow as Ui_Q5
except ImportError as e:
    print(f"Error: No se encontró el archivo {e.name} en la carpeta 'Pantallas'.")
    print("Asegúrate de que la carpeta se llame 'Pantallas' y tenga un archivo __init__.py")
    sys.exit()

# --- Clase Controladora Principal ---
class CursoGit(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.mostrar_inicio()

    def limpiar_ventana(self):
        # Crea un nuevo widget central limpio para cada pantalla
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

    def mostrar_inicio(self):
        self.ui = Ui_Pantalla_De_Inicio()
        self.ui.setupUi(self)
        # Conectar botón (ajusta el nombre del botón según tu .py si es necesario)
        if hasattr(self.ui, 'pushButton'):
            self.ui.pushButton.clicked.connect(self.mostrar_bienvenida)
        self.show()

    def mostrar_bienvenida(self):
        self.limpiar_ventana()
        self.ui = Ui_Bienvenida()
        self.ui.setupUi(self)
        if hasattr(self.ui, 'pushButton'):
            self.ui.pushButton.clicked.connect(self.mostrar_seccion2)

    def mostrar_seccion2(self):
        self.limpiar_ventana()
        self.ui = Ui_Seccion2()
        self.ui.setupUi(self)
        if hasattr(self.ui, 'pushButton_2'):
            self.ui.pushButton_2.clicked.connect(self.iniciar_lecciones)

    def iniciar_lecciones(self):
        # Aquí puedes crear una lógica para ir pasando de Lección 1 a la 7
        self.mostrar_leccion(1)

    def mostrar_leccion(self, num):
        self.limpiar_ventana()
        # Diccionario de lecciones para facilitar el cambio
        lecciones = {
            1: Ui_Leccion1, 2: Ui_Leccion2, 3: Ui_Leccion3,
            4: Ui_Leccion4, 5: Ui_Leccion5, 6: Ui_Leccion6, 7: Ui_Leccion7
        }
        
        ClaseLeccion = lecciones.get(num)
        self.ui = ClaseLeccion()
        self.ui.setupUi(self)
        
        # Lógica para el botón "Siguiente"
        # Buscamos 'pushButton' o 'pushButton_2' que sueles usar para avanzar
        boton = getattr(self.ui, 'pushButton', getattr(self.ui, 'pushButton_2', None))
        if boton:
            if num < 7:
                boton.clicked.connect(lambda: self.mostrar_leccion(num + 1))
            else:
                boton.clicked.connect(self.mostrar_quiz_intro)

    def mostrar_quiz_intro(self):
        self.limpiar_ventana()
        self.ui = Ui_Leccion8()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(lambda: self.mostrar_pregunta(1))

    def mostrar_pregunta(self, num):
        self.limpiar_ventana()
        quices = {1: Ui_Q1, 2: Ui_Q2, 3: Ui_Q3, 4: Ui_Q4, 5: Ui_Q5}
        self.ui = quices[num]()
        self.ui.setupUi(self)
        
        boton_sig = getattr(self.ui, 'pushButton_2', getattr(self.ui, 'pushButton_6', None))
        if boton_sig:
            if num < 5:
                boton_sig.clicked.connect(lambda: self.mostrar_pregunta(num + 1))
            else:
                boton_sig.clicked.connect(self.finalizar)

    def finalizar(self):
        QtWidgets.QMessageBox.information(self, "Fin", "¡Felicidades! Has terminado el curso.")
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CursoGit()
    sys.exit(app.exec_())