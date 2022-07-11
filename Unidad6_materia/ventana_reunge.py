import sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication
from PyQt5 import uic
from PyQt5 import QtWidgets
import ctypes #getSystemMetr

#importaciones propias
from Unidad6_materia.unidad6.Metodo_Runge import Metodo_Runge_cuarto_grado

class Ventana_runge(QDialog):

    def __init__(self, ventana_principal):

        self.ventana_principal = ventana_principal

        QDialog.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("Unidad6_materia/ventana_de_runge.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)

        header1 = self.mitabla.horizontalHeader()       
        header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        #boton 
        self.btnaceptar.clicked.connect(self.metodo)


    def metodo(self):

        x1 = self.valorA1.text()
        x2 = self.valorA2.text()
        y = self.valorY.text()
        h = self.valorH.text()
        ecuacion = self.ecuacion.text()
        
        if(x1 != "" and y != "" and h != "" and ecuacion != "" and x2 != ""):

            instancia = Metodo_Runge_cuarto_grado()
            resultados = instancia.proceso(float(x1),float(y),ecuacion,float(h),float(x2))
            #coloca los resultados en la tabla
            self.mitabla.setRowCount(len(resultados))
            row = 0
            for columna in resultados:
                
                self.mitabla.setItem(row,0, QtWidgets.QTableWidgetItem(str(columna[0])))
                self.mitabla.setItem(row,1, QtWidgets.QTableWidgetItem("{:.4f}".format(columna[1])))
                self.mitabla.setItem(row,2, QtWidgets.QTableWidgetItem("{:.4f}".format(columna[2])))

                self.mitabla.setItem(row,3, QtWidgets.QTableWidgetItem("{:.4f}".format(columna[3])))
                self.mitabla.setItem(row,4, QtWidgets.QTableWidgetItem("{:.4f}".format(columna[4])))
                self.mitabla.setItem(row,5, QtWidgets.QTableWidgetItem("{:.4f}".format(columna[5])))
                self.mitabla.setItem(row,6, QtWidgets.QTableWidgetItem("{:.4f}".format(columna[6])))
               
               
                row+=1

        else:

            QMessageBox.warning(self, "hey !!", "Debes rellenar todos los campos", QMessageBox.Discard)

       



    def closeEvent(self, event):

        self.ventana_principal.show()

