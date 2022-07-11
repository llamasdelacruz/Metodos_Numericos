
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic, QtGui
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
import ctypes

from sympy import Integer #getSystemMetr

#imports codigo propio
from Unidad3_materia.unidad3.Metodo_Jacobi_real import Jacobi
from Unidad3_materia.unidad3.Metodo_Gauss_seiden import Gauss

class Ventana_gauss_jacobi(QMainWindow):

    def __init__(self, ventana_principal):

        self.ventana_principal = ventana_principal

        QMainWindow.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("Unidad3_materia/ventana_gauss_jacobi.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)

        #botones
        self.boton_gauss.clicked.connect(self.establecer_titulo_gauss)
        self.boton_jacobi.clicked.connect(self.estabalecer_titulo_jacobi)

        #variables globales
        self.jacobi_conexion = Jacobi()
        self.gauss_conexion = Gauss()

        
    def establecer_titulo_gauss(self):


        if(self.expresion1.text() != "" and self.expresion2.text() != "" and self.expresion3.text() != "" and self.numero_iteraciones.text() != ""):

            self.mitabla.setColumnCount(4)
            self.mitabla.setHorizontalHeaderLabels (['x', 'y', 'z', 'Di'])

            lista_expresiones =[self.expresion1.text(), self.expresion2.text(), self.expresion3.text()]
            
            lista_xyz = self.gauss_conexion.valores_ecuacion_buscar_expreciones_regulares(self.valores_iniciales.text())
            
            resultados = self.gauss_conexion.proceso_seiden(lista_expresiones, lista_xyz[0], lista_xyz[1], lista_xyz[2], int(self.numero_iteraciones.text()) )

            row = 0
            
            self.mitabla.setRowCount(len(resultados))
            for columna in resultados:
                
                self.mitabla.setItem(row,0, QtWidgets.QTableWidgetItem(str(columna[0])))
                self.mitabla.setItem(row,1, QtWidgets.QTableWidgetItem(str(columna[1])))
                self.mitabla.setItem(row,2, QtWidgets.QTableWidgetItem(str(columna[2])))
                self.mitabla.setItem(row,3, QtWidgets.QTableWidgetItem(str(columna[3])))
               
               
                row+=1

        elif(self.expresion1.text() != "" and self.expresion2.text() != "" and self.expresion3.text() == "" and self.numero_iteraciones.text() != ""):

            self.mitabla.setColumnCount(3)
            self.mitabla.setHorizontalHeaderLabels (['x', 'y', 'Di'])

            lista_expresiones =[self.expresion1.text(), self.expresion2.text()]
            
            lista_xyz = self.gauss_conexion.valores_ecuacion_buscar_expreciones_regulares(self.valores_iniciales.text())
            
            resultados = self.gauss_conexion.proceso_seiden(lista_expresiones, lista_xyz[0], lista_xyz[1], 0,int(self.numero_iteraciones.text()))

            row = 0
            
            self.mitabla.setRowCount(len(resultados))
            for columna in resultados:
                
                self.mitabla.setItem(row,0, QtWidgets.QTableWidgetItem(str(columna[0])))
                self.mitabla.setItem(row,1, QtWidgets.QTableWidgetItem(str(columna[1])))
                self.mitabla.setItem(row,2, QtWidgets.QTableWidgetItem(str(columna[2])))
               
                row+=1

    def estabalecer_titulo_jacobi(self):

        if(self.expresion1.text() != "" and self.expresion2.text() != "" and self.expresion3.text() != "" and self.numero_iteraciones.text() != ""):

            self.mitabla.setColumnCount(4)
            self.mitabla.setHorizontalHeaderLabels (['x', 'y', 'z', 'Di'])

            lista_expresiones =[self.expresion1.text(), self.expresion2.text(), self.expresion3.text()]
            
            lista_xyz = self.jacobi_conexion.valores_ecuacion_buscar_expreciones_regulares(self.valores_iniciales.text())
            
            resultados = self.jacobi_conexion.proceso_jacobi(lista_expresiones, lista_xyz[0], lista_xyz[1], lista_xyz[2], int(self.numero_iteraciones.text()))

            row = 0
            
            self.mitabla.setRowCount(len(resultados))
            for columna in resultados:
                
                self.mitabla.setItem(row,0, QtWidgets.QTableWidgetItem(str(columna[0])))
                self.mitabla.setItem(row,1, QtWidgets.QTableWidgetItem(str(columna[1])))
                self.mitabla.setItem(row,2, QtWidgets.QTableWidgetItem(str(columna[2])))
                self.mitabla.setItem(row,3, QtWidgets.QTableWidgetItem(str(columna[3])))
               
                row+=1

        elif(self.expresion1.text() != "" and self.expresion2.text() != "" and self.expresion3.text() == "" and self.numero_iteraciones.text() != ""):

            self.mitabla.setColumnCount(3)
            self.mitabla.setHorizontalHeaderLabels (['x', 'y', 'Di'])

            lista_expresiones =[self.expresion1.text(), self.expresion2.text()]
            
            lista_xyz = self.jacobi_conexion.valores_ecuacion_buscar_expreciones_regulares(self.valores_iniciales.text())
            
            resultados = self.jacobi_conexion.proceso_jacobi(lista_expresiones, lista_xyz[0], lista_xyz[1], 0, int(self.numero_iteraciones.text()))

            row = 0
            
            self.mitabla.setRowCount(len(resultados))
            for columna in resultados:
                
                self.mitabla.setItem(row,0, QtWidgets.QTableWidgetItem(str(columna[0])))
                self.mitabla.setItem(row,1, QtWidgets.QTableWidgetItem(str(columna[1])))
                self.mitabla.setItem(row,2, QtWidgets.QTableWidgetItem(str(columna[2])))
               
                row+=1





    def closeEvent(self, event):

        self.ventana_principal.show()
        
        

if(__name__ == "__main__"):

    #Instancia para iniciar la aplicacion
    app = QApplication(sys.argv)
    ventana = Ventana_gauss_jacobi()
    ventana.show()
    #ejecutar la aplicacion
    app.exec_()