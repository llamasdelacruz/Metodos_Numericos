from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
import ctypes #getSystemMetr

#imports codigo propio
#se debe poner toda la ruta desde el paqute raiz para que python lo capte
from Unidad4_materia.vantana_integracion import Ventana_integracion
from Unidad4_materia.ventana_derivacion import Ventana_derivacion
from Unidad4_materia.ventana_derivacion2 import Ventana_derivacion2


class Ventana_unidad4(QDialog):

    def __init__(self, ventana_principal):

        self.ventana_principal = ventana_principal

        QDialog.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("Unidad4_materia/ventana_unidad4.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)

        # le da funcionalidad a los botones
        self.derivacion.clicked.connect(self.llamar_derivacion)
        self.derivacion_2.clicked.connect(self.llamar_derivacion2)
        self.integracion.clicked.connect(self.llamada_integracion)


    def llamar_derivacion(self):
        self.hide()
        self.ex = Ventana_derivacion(self)
        self.ex.show()

    def llamar_derivacion2(self):
        self.hide()
        self.ex = Ventana_derivacion2(self)
        self.ex.show()

    def llamada_integracion(self):
        
        self.hide()
        self.ex = Ventana_integracion(self)
        self.ex.show()


    


    def closeEvent(self, event):

        self.ventana_principal.show()
        