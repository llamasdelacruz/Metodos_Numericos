
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont #fuentes
import ctypes #getSystemMetr

#imports codigo propio
from Unidad2_materia.metodosDeResolucionDeEcuaciones.metodoGrafico import Grafico_metodo
from Unidad2_materia.metodosDeResolucionDeEcuaciones.metodoIgualacion import Igualacion_metodo
from Unidad2_materia.metodosDeResolucionDeEcuaciones.metodoReduccion import Reduccion_Metodo
from Unidad2_materia.metodosDeResolucionDeEcuaciones.metodoSustitucion import Sustitucion_metodo


class Ventana_ecuaciones(QMainWindow):

    def __init__(self, ventana_principal):

        self.ventana_principal = ventana_principal

        QMainWindow.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("Unidad2_materia/VentanaEcuaciones.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)

        self.sustitucion.clicked.connect(self.sustitucion_metodo)
        self.reduccion.clicked.connect(self.reduccion_metodo)
        self.igualacion.clicked.connect(self.igualacion_metodo)
        self.grafico.clicked.connect(self.grafico_metodo)


    def sustitucion_metodo(self):

        lista = []

        objeto1 = Sustitucion_metodo()
        sentencia1 = self.ecuacion1.text()
        sentencia2 = self.ecuacion2.text()
        lista.append(objeto1.valores_ecuacion_buscar(sentencia1))
        lista.append(objeto1.valores_ecuacion_buscar(sentencia2))

        resultado = objeto1.proceso_sustitucion(lista)

        self.Resultado.setText("Sustitucion: x = " + str(resultado[0]) + ", y = " + str(resultado[1]))
        self.Resultado.adjustSize()


    def reduccion_metodo(self):

        lista = []

        objeto1 = Reduccion_Metodo()
        sentencia1 = self.ecuacion1.text()
        sentencia2 = self.ecuacion2.text()
        lista.append(objeto1.valores_ecuacion_buscar(sentencia1))
        lista.append(objeto1.valores_ecuacion_buscar(sentencia2))

        resultado = objeto1.obtener_puntos(lista)
        self.Resultado.setText(" Reduccion: x = " + str(resultado[0]) + ", y = " + str(resultado[1]))
        self.Resultado.adjustSize()

    def igualacion_metodo(self):
        lista = []

        objeto1 = Igualacion_metodo()
        sentencia1 = self.ecuacion1.text()
        sentencia2 = self.ecuacion2.text()
        lista.append(objeto1.valores_ecuacion_buscar(sentencia1))
        lista.append(objeto1.valores_ecuacion_buscar(sentencia2))

        resultado = objeto1.proceso_igualacion(lista)

        self.Resultado.setText("Igualacion: x = " + str(resultado[0]) + ", y = " + str(resultado[1]))
        self.Resultado.adjustSize()

    def grafico_metodo(self):

        lista = []
        objeto1 = Grafico_metodo()
        sentencia1 = self.ecuacion1.text()
        sentencia2 = self.ecuacion2.text()
        lista.append(objeto1.valores_ecuacion_buscar(sentencia1))
        lista.append(objeto1.valores_ecuacion_buscar(sentencia2))
        objeto1.grafica(lista)


    def closeEvent(self, event):

        self.ventana_principal.show()
        
        
        

if(__name__ == "__main__"):

    #Instancia para iniciar la aplicacion
    app = QApplication(sys.argv)
    ventana = Ventana_ecuaciones()
    ventana.show()
    #ejecutar la aplicacion
    app.exec_()