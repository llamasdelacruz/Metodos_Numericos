from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic
from PyQt5 import QtWidgets
import ctypes #getSystemMetr

#imports codigo propio
#se debe poner toda la ruta desde el paqute raiz para que python lo capte
from Unidad4_materia.unidad4.Metodo_integracion_trapecios import Metodo_integracion_trapecios
from Unidad4_materia.unidad4.Metodo_simpson_1_3 import Metodo_simpson_1_3
from Unidad4_materia.unidad4.Metodo_simpson_3_8 import Metodo_simpson_3_8
from Unidad4_materia.unidad4.Metodo_cuadratura_gaussiana import Cuadratura_gauss


class Ventana_integracion(QDialog):

    def __init__(self, ventana_principal):

        self.ventana_principal = ventana_principal

        QDialog.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("Unidad4_materia/ventana_integracion.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)

        # le da funcionalidad a los botones
        self.boton_trapecios.clicked.connect(self.proceso_integracion_trapecios)
        self.boton_simpson1_3.clicked.connect(self.proceso_simpson_1_3)
        self.boton_simpson3_8.clicked.connect(self.proceso_simpson_3_8)
        self.cuadratura_gauss.clicked.connect(self.proceso_cuadratura_gaussiana)

        # haciendo instancias de las clases
        self.conexion_trapecios = Metodo_integracion_trapecios()
        self.conexion_simpson13 = Metodo_simpson_1_3()
        self.conexion_simpson38 = Metodo_simpson_3_8()
        self.conexion_cuadratura_gausiana = Cuadratura_gauss()


    def proceso_integracion_trapecios(self):

        if(self.ecuacion.text() != "" and self.valorA.text() != "" and self.valorB.text() != ""):

            resultados = self.conexion_trapecios.proceso(self.ecuacion.text(), float(self.valorA.text()), float(self.valorB.text()))

            self.mitabla.setRowCount(1)
            
                
            self.mitabla.setItem(0,0, QtWidgets.QTableWidgetItem(str("{:.6f}".format(resultados[0]))))
            self.mitabla.setItem(0,1, QtWidgets.QTableWidgetItem(str("{:.6f}".format(resultados[1]))))
            self.mitabla.setItem(0,2, QtWidgets.QTableWidgetItem(str("{:.6f}".format(resultados[2]))))
               
               
        
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


    def proceso_simpson_1_3(self):
        
        if(self.ecuacion.text() != "" and self.valorA.text() != "" and self.valorB.text() != ""):

            resultados = self.conexion_simpson13.proceso(self.ecuacion.text(), float(self.valorA.text()), float(self.valorB.text()))

            # establecemos el numero de filas que queremos colocar en la tabla que tenemos
            self.mitabla.setRowCount(1)

            # colocar los items
            self.mitabla.setItem(0,0, QtWidgets.QTableWidgetItem(str("{:.6f}".format(resultados[0]))))
            self.mitabla.setItem(0,1, QtWidgets.QTableWidgetItem(str("{:.6f}".format(resultados[1]))))
            self.mitabla.setItem(0,2, QtWidgets.QTableWidgetItem(str("{:.6f}".format(resultados[2]))))

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


    def proceso_simpson_3_8(self):

        if(self.ecuacion.text() != "" and self.valorA.text() != "" and self.valorB.text() != ""):

            resultados = self.conexion_simpson38.proceso(self.ecuacion.text(), float(self.valorA.text()), float(self.valorB.text()))

            self.mitabla.setRowCount(1)

            # colocar los items
            self.mitabla.setItem(0,0, QtWidgets.QTableWidgetItem(str("{:.6f}".format(resultados[0]))))
            self.mitabla.setItem(0,1, QtWidgets.QTableWidgetItem(str("{:.6f}".format(resultados[1]))))
            self.mitabla.setItem(0,2, QtWidgets.QTableWidgetItem(str("{:.6f}".format(resultados[2]))))

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

    def proceso_cuadratura_gaussiana(self):

        
        if(self.ecuacion.text() != "" and self.valorA.text() != "" and self.valorB.text() != ""):

            self.mitabla.setRowCount(1)
            # la cntidad de puntos a usar
            numero_puntos = self.numero_puntos.value()
            resultado = self.conexion_cuadratura_gausiana.proceso(float(self.valorA.text()), float(self.valorB.text()), self.ecuacion.text(), numero_puntos)
            # colocar los items
            self.mitabla.setItem(0,1, QtWidgets.QTableWidgetItem( str(resultado) ) )
        

        else:
           
           QMessageBox.warning(self, "hey !!", "Debes rellenar todos los campos", QMessageBox.Discard)

    def closeEvent(self, event):

        self.ventana_principal.show()
        