
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont #fuentes
import ctypes

from Unidad2_materia.ventana_ecuaciones import Ventana_ecuaciones
from Unidad2_materia.ventana_intervalos import Ventana_intervalos #getSystemMetr

class Ventana(QMainWindow):

    def __init__(self, ventana_principal):

        self.ventana_principal = ventana_principal

        QMainWindow.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("Unidad2_materia/VentanaPrincipal.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)

        self.MetodosDeIntervalo.clicked.connect(self.metodos_intervalo)
        self.SolucionDeEcuaciones.clicked.connect(self.metodos_solucion_ecuaciones)

    def metodos_intervalo(self):
        self.hide()
        self.ex = Ventana_intervalos(self)
        self.ex.show()

    def metodos_solucion_ecuaciones(self):
        self.hide()
        self.ex = Ventana_ecuaciones(self)
        self.ex.show()

    
    def closeEvent(self, event):

        self.ventana_principal.show()
