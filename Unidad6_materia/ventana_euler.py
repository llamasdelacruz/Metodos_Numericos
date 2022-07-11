import sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication
from PyQt5 import uic
from PyQt5 import QtWidgets
import ctypes #getSystemMetr

#importaciones propias
from Unidad6_materia.unidad6.Metodo_euler import Metodo_Euler

class Ventana_euler(QDialog):

    def __init__(self, ventana_principal):

        self.ventana_principal = ventana_principal

        QDialog.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("Unidad6_materia/ventana_de_euler.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)

        header1 = self.mitabla.horizontalHeader()       
        header1.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        #boton 
        self.btnaceptar.clicked.connect(self.metodo)


    def metodo(self):

        x = self.valorA1.text()
        y = self.valorY.text()
        h = self.valorH.text()
        iteraciones = self.valorI.text()
        ecuacion = self.ecuacion.text()
        
        if(x != "" and y != "" and h != "" and iteraciones != "" and ecuacion != ""):
            instancia = Metodo_Euler()
            resultados = instancia.proceso_euler(float(x),float(y),float(h),ecuacion,int(iteraciones))

            #coloca los resultados en la tabla
            self.mitabla.setRowCount(len(resultados))
            row = 0
            for columna in resultados:
                
                self.mitabla.setItem(row,0, QtWidgets.QTableWidgetItem(str("{:.6f}".format(columna[0]))))
                self.mitabla.setItem(row,1, QtWidgets.QTableWidgetItem(str("{:.6f}".format(columna[1]))))
                self.mitabla.setItem(row,2, QtWidgets.QTableWidgetItem(str("{:.6f}".format(columna[2]))))

                self.mitabla.setItem(row,3, QtWidgets.QTableWidgetItem(str("{:.6f}".format(columna[3]))))
               
               
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
