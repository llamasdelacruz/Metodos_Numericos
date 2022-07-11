import re
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel
from PyQt5 import uic #para abrir las interfaces .uic
import ctypes
from PyQt5 import QtWidgets

from Unidad3_materia.unidad3.Metodo_Newton_real import Newton
from Unidad3_materia.unidad3.Metodo_punto_fijo import Punto_fijo


#crear una ventana de dialogo
class Ventana_Newton(QDialog):


    def __init__(self, ventana_principal):

        QDialog.__init__(self)

        self.ventana_principal = ventana_principal

        #QMainWindow.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("Unidad3_materia/ventana_metodo_newton.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)

        #botones
        self.boton_newton.clicked.connect(self.ejecutar_newton)
        self.boton_puntofijo.clicked.connect(self.ejecutar_punto_fijo)

        #variables
        self.Newton_conexion = Newton()
        self.punto_fijo_conexion = Punto_fijo()
        

    def ejecutar_newton(self):

        self.mitabla.setColumnCount(3)
        self.mitabla.setHorizontalHeaderLabels (['x', 'y', 'e'])

        if(self.expresion1.text() != "" and self.expresion2.text() != "" and self.valores.text() != "" and self.iteraciones.text() != ""):
            
            lista_valores = [float(s) for s in re.findall(r'-?\d+\.?\d?', self.valores.text())]
            resultados = self.Newton_conexion.proceso(self.expresion1.text(), self.expresion2.text(), lista_valores[0], lista_valores[1], int(self.iteraciones.text()) )
            row = 0
            
            self.mitabla.setRowCount(len(resultados))
            for columna in resultados:
                
                self.mitabla.setItem(row,0, QtWidgets.QTableWidgetItem(str("{:.4f}".format(columna[0][0]))))
                self.mitabla.setItem(row,1, QtWidgets.QTableWidgetItem(str("{:.4f}".format(columna[0][1]))))
                self.mitabla.setItem(row,2, QtWidgets.QTableWidgetItem(str("{:.4f}".format(columna[1]))))
               
               
                row+=1

    def ejecutar_punto_fijo(self):

        self.mitabla.setColumnCount(2)
        self.mitabla.setHorizontalHeaderLabels (['x', 'y'])

        if(self.expresion1.text() != "" and self.expresion2.text() != "" and self.valores.text() != "" and self.iteraciones.text() != ""):
            
            lista_valores = [float(s) for s in re.findall(r'-?\d+\.?\d?', self.valores.text())]
            resultados = self.punto_fijo_conexion.proceso_punto_fijo(self.expresion1.text(), self.expresion2.text(), lista_valores[0], lista_valores[1], int(self.iteraciones.text()) )
            row = 0
            
            self.mitabla.setRowCount(len(resultados))
            for columna in resultados:
                
                self.mitabla.setItem(row,0, QtWidgets.QTableWidgetItem(str("{:.4f}".format(columna[0]))))
                self.mitabla.setItem(row,1, QtWidgets.QTableWidgetItem(str("{:.4f}".format(columna[1]))))      
               
                row+=1




        

    def closeEvent(self, event):

        self.ventana_principal.show()