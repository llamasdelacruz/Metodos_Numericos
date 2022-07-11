
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import ctypes
from Unidad2_materia.VentanaUnidad2Inicio import Ventana
from Unidad3_materia.ventana_unidad3 import Ventana_unidad3
from Unidad4_materia.ventana_unidad4 import Ventana_unidad4
from Unidad5_materia.ventana_unidad5 import Ventana_unidad5
from Unidad6_materia.ventana_unidad6 import Ventana_unidad6

class Ventana_principal(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("Ventana_principal_del_proyecto.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)
        self.Aceptar.clicked.connect(self.eleccion)

    
    def eleccion(self):
        
        if(self.Unidades.currentIndex() == 0):

            self.hide()
            self.ex = Ventana(self)
            self.ex.show()

        elif(self.Unidades.currentIndex() == 1):

            self.hide()
            self.ex = Ventana_unidad3(self)
            self.ex.show()

        elif(self.Unidades.currentIndex() == 2):

            self.hide()
            self.ex = Ventana_unidad4(self)
            self.ex.show()

        elif(self.Unidades.currentIndex() == 3):

            self.hide()
            self.ex = Ventana_unidad5(self)
            self.ex.show()

        elif(self.Unidades.currentIndex() == 4):

            self.hide()
            self.ex = Ventana_unidad6(self)
            self.ex.show()
        

if(__name__ == "__main__"):

    #Instancia para iniciar la aplicacion
    app = QApplication(sys.argv)
    ventana = Ventana_principal()
    ventana.show()
    #ejecutar la aplicacion
    app.exec_()