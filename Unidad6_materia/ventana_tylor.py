import sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication
from PyQt5 import uic
from PyQt5 import QtWidgets
import ctypes #getSystemMetr

#importaciones propias
from Unidad6_materia.unidad6.Metodo_taylor import Serie_Taylor

class Ventana_tylor(QDialog):

    def __init__(self, ventana_principal):

        self.ventana_principal = ventana_principal

        QDialog.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("Unidad6_materia/ventana_de_tylor.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)


        #boton 
        self.btnaceptar.clicked.connect(self.metodo)


    def metodo(self):

        x1 = self.valorA1.text()
        n = self.valorT.text()
        ecuacion = self.ecuacion.text()
        
        if(x1 != "" and ecuacion != "" and n != ""):
            instancia = Serie_Taylor()
            resultados = instancia.proceso(int(n),float(x1),ecuacion)
            self.resultadolabel.setText(str(resultados))
            self.resultadolabel.adjustSize()
            

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
