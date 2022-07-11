import sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication
from PyQt5 import uic
from PyQt5 import QtWidgets
import ctypes #getSystemMetr

#importaciones propias
from Unidad6_materia.ventana_euler import Ventana_euler
from Unidad6_materia.ventana_heun import Ventana_heun
from Unidad6_materia.ventana_tylor import Ventana_tylor
from Unidad6_materia.ventana_reunge import Ventana_runge

class Ventana_unidad6(QDialog):

    def __init__(self, ventana_principal):

        self.ventana_principal = ventana_principal

        QDialog.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("Unidad6_materia/ventana_unidad6.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)

        self.btneuler.clicked.connect(self.llamar_euler)
        self.btnheun.clicked.connect(self.llamar_heun)
        self.btntylor.clicked.connect(self.llamada_tylor)
        self.btnrunge.clicked.connect(self.llamada_runge)

        #boton 
    def llamar_euler(self):
        self.hide()
        self.ex = Ventana_euler(self)
        self.ex.show()

    def llamar_heun(self):
        self.hide()
        self.ex = Ventana_heun(self)
        self.ex.show()

    def llamada_tylor(self):
        
        self.hide()
        self.ex = Ventana_tylor(self)
        self.ex.show()

    def llamada_runge(self):
        
        self.hide()
        self.ex = Ventana_runge(self)
        self.ex.show()
       



    def closeEvent(self, event):

        self.ventana_principal.show()



if(__name__ == "__main__"):

    #Instancia para iniciar la aplicsacion
    app = QApplication(sys.argv)
    ventana = Ventana_euler()
    ventana.show()
    #ejecutar la aplicacion
    app.exec_()
