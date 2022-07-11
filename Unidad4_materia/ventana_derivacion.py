from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic
from PyQt5 import QtWidgets
import ctypes #getSystemMetr

#imports codigo propio
#se debe poner toda la ruta desde el paqute raiz para que python lo capte
from Unidad4_materia.unidad4.Metodo_derivacion import Metodo_derivacion

class Ventana_derivacion(QDialog):

    def __init__(self, ventana_principal):

        self.ventana_principal = ventana_principal

        QDialog.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("Unidad4_materia/ventana_derivacion.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)

        # le da funcionalidad a los botones
            # le da funcionalidad a los botones
        self.boton_aceptar.clicked.connect(self.proceso)
        self.conexionClaseDerivacion = Metodo_derivacion()


    def proceso(self):

        if(self.ecuacion.text() != "" and self.valorX.text() != "" and self.valorH.text() != "" and self.numero_iteraciones.text() != "" ):

            resultados = self.conexionClaseDerivacion.proceso(self.ecuacion.text(), float(self.valorX.text()), float(self.valorH.text()), int(self.numero_iteraciones.text()))

            self.mitabla.setRowCount(len(resultados))
            row = 0
            for columna in resultados:
                
                self.mitabla.setItem(row,0, QtWidgets.QTableWidgetItem(str("{:.6f}".format(columna[0]))))
                self.mitabla.setItem(row,1, QtWidgets.QTableWidgetItem(str("{:.6f}".format(columna[1]))))
                self.mitabla.setItem(row,2, QtWidgets.QTableWidgetItem(str("{:.6f}".format(columna[2]))))

                self.mitabla.setItem(row,3, QtWidgets.QTableWidgetItem(str("{:.6f}".format(columna[3]))))
                self.mitabla.setItem(row,4, QtWidgets.QTableWidgetItem(str("{:.6f}".format(columna[4]))))
                self.mitabla.setItem(row,5, QtWidgets.QTableWidgetItem(str("{:.6f}".format(columna[5]))))

                self.mitabla.setItem(row,6, QtWidgets.QTableWidgetItem(str("{:.6f}".format(columna[6]))))
                self.mitabla.setItem(row,7, QtWidgets.QTableWidgetItem(str("{:.6f}".format(columna[7]))))
               
               
                row+=1

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
        
            # setting message for Message Box
            msg.setText("Debes rellenar todos los campos")
            
            # setting Message box window title
            msg.setWindowTitle("Warning MessageBox")
            
            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
            # start the app
            retval = msg.exec_()

    def closeEvent(self, event):

        self.ventana_principal.show()
        