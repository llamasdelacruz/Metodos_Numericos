import sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication
from PyQt5 import uic
from PyQt5 import QtWidgets
import ctypes #getSystemMetr

#importaciones propias
from Unidad6_materia.unidad6.Metodo_de_heun import Metodo_de_Heun

class Ventana_heun(QDialog):

    def __init__(self, ventana_principal):

        self.ventana_principal = ventana_principal

        QDialog.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("Unidad6_materia/ventana_de_heun.ui", self)

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
        error = self.valorE.text()
        ecuacion = self.ecuacion.text()
        
        if(x1 != "" and y != "" and h != "" and error != "" and ecuacion != "" and x2 != ""):

            instancia = Metodo_de_Heun()
            resultados = instancia.proceso(float(h),float(x1),float(x2),float(y),ecuacion,float(error))
            #coloca los resultados en la tabla
            self.mitabla.setRowCount(len(resultados))
            row = 0
            for columna in resultados:
                
                self.mitabla.setItem(row,0, QtWidgets.QTableWidgetItem(str(columna[0])))
                self.mitabla.setItem(row,1, QtWidgets.QTableWidgetItem(str(columna[1])))
                self.mitabla.setItem(row,2, QtWidgets.QTableWidgetItem(str(columna[2])))

                self.mitabla.setItem(row,3, QtWidgets.QTableWidgetItem(str(columna[3])))
                self.mitabla.setItem(row,4, QtWidgets.QTableWidgetItem(str(columna[4])))
                self.mitabla.setItem(row,5, QtWidgets.QTableWidgetItem(str(columna[5])))

                self.mitabla.setItem(row,6, QtWidgets.QTableWidgetItem(str(columna[6])))
                self.mitabla.setItem(row,7, QtWidgets.QTableWidgetItem(str(columna[7])))
                
               
               
                row+=1

        else:

            QMessageBox.warning(self, "hey !!", "Debes rellenar todos los campos", QMessageBox.Discard)

       



    def closeEvent(self, event):

        self.ventana_principal.show()



if(__name__ == "__main__"):

    #Instancia para iniciar la aplicsacion
    app = QApplication(sys.argv)
    ventana = Ventana_euler()
    ventana.show()
    #ejecutar la aplicacion
    app.exec_()
