
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont #fuentes
import ctypes #getSystemMetr

#imports codigo propio
#se debe poner toda la ruta desde el paqute raiz para que python lo capte
from Unidad3_materia.ventana_Gauss_Jacobi import Ventana_gauss_jacobi
from Unidad3_materia.ventana_metodo_newton import Ventana_Newton


class Ventana_unidad3(QMainWindow):

    def __init__(self, ventana_principal):

        self.ventana_principal = ventana_principal

        QMainWindow.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("Unidad3_materia/ventana_unidad3.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)

        self.Jacobi_Gauss.clicked.connect(self.llamar_jacobi_gauss)
        self.Newton.clicked.connect(self.llamada_newton)

    def llamar_jacobi_gauss(self):
        self.hide()
        self.ex = Ventana_gauss_jacobi(self)
        self.ex.show()

    def llamada_newton(self):
        
        self.hide()
        self.ex = Ventana_Newton(self)
        self.ex.show()


    def closeEvent(self, event):

        self.ventana_principal.show()
        