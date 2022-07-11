from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic
from PyQt5 import QtWidgets
import ctypes #getSystemMetr
import numpy as np

# mis clases 
from Unidad5_materia.unidad5.Interpolacion_lagrange import Interpolacion_lagrange
from Unidad5_materia.unidad5.Interpolacion_newton import Interpolacion_newton
from Unidad5_materia.unidad5.metodo_minimos_cuadrados import Metodos_minimos_cuadrados
from Unidad5_materia.unidad5.Resgresion_lineal_simple import Regresion_lineal

class Ventana_unidad5(QDialog):

    def __init__(self, ventana_principal):

        self.ventana_principal = ventana_principal

        QDialog.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("Unidad5_materia/ventana_unidad5.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)

        # instancias
        self.interpolacionl = Interpolacion_lagrange()
        self.interpolacionN = Interpolacion_newton()
        self.minimosC = Metodos_minimos_cuadrados()
        self.regresionl = Regresion_lineal()

        # conexion botones
        self.btnmas.clicked.connect(self.agregar_filas)
        self.btnmenos.clicked.connect(self.eliminar_filas)
        self.btnnewton.clicked.connect(self.funcion_newton)
        self.btnlagrange.clicked.connect(self.funcion_lagrange)
        self.btnregresion.clicked.connect(self.funcion_regresion)
        self.btnminimos.clicked.connect(self.funcion_minimos)
        self.btngraficar.clicked.connect(self.graficar_funcion)
        self.btncalcular.clicked.connect(self.sacar_valor_x)


    def funcion_newton(self):
        #ejecuta el proceso de newton
        numero_filas = self.mitabla.rowCount()
        numero_columnas = numero_filas+1
        matriz = self.tomar_valores_tabla(np.zeros((numero_filas, numero_columnas)))

        ecuacion = self.interpolacionN.encontra_ecuacion(matriz, numero_filas)

        self.resultado.setText(ecuacion)
        self.resultado.adjustSize()
        self.error.setText("")
        self.error.adjustSize()
        


    def funcion_lagrange(self):
        
        numero_filas = self.mitabla.rowCount()
        numero_columnas = 2
        matriz = self.tomar_valores_tabla(np.zeros((numero_filas, numero_columnas)))

        ecuacion = self.interpolacionl.proceso_lagrange(matriz,numero_filas)

        self.resultado.setText(ecuacion)
        self.resultado.adjustSize()
        self.error.setText("")
        self.error.adjustSize()


    def funcion_regresion(self):

        numero_filas = self.mitabla.rowCount()
        numero_columnas = 2
        matriz = self.tomar_valores_tabla(np.zeros((numero_filas, numero_columnas)))

        ecuacion,error_e = self.regresionl.proceso_regresion(matriz,numero_filas)

        self.resultado.setText(ecuacion)
        self.resultado.adjustSize()
        self.error.setText("Error:"+str(error_e))
        self.error.adjustSize()

    def funcion_minimos(self):

        numero_filas = self.mitabla.rowCount()
        numero_columnas = 2
        matriz = self.tomar_valores_tabla(np.zeros((numero_filas, numero_columnas)))

        ecuacion = self.minimosC.proceso(matriz,numero_filas)

        self.resultado.setText(ecuacion)
        self.resultado.adjustSize()
        self.error.setText("")
        self.error.adjustSize()

    def graficar_funcion(self):
        try:
            ecuacion = self.resultado.text()
            self.interpolacionN.graficar_ecuacion(ecuacion)
        except:
            pass
        

    def sacar_valor_x(self):

        x = float(self.Punto.text())
        ecuacion = self.resultado.text()

        y = self.interpolacionN.evaluacion(x,ecuacion)
        self.resultado2.setText(str(y))
        self.resultado2.adjustSize()




    def agregar_filas(self):

        posicion_fila = self.mitabla.rowCount()
        self.mitabla.insertRow(posicion_fila)

    def eliminar_filas(self):

        posicion_fila = self.mitabla.rowCount()
        self.mitabla.removeRow(posicion_fila-1)


    def tomar_valores_tabla(self, matriz):
        
        for i in range(self.mitabla.rowCount()):

            for j in range(2):

                valor_celda = self.mitabla.item(i, j)
                matriz[i][j] = float(valor_celda.text())


        return matriz
                



    def closeEvent(self, event):

        self.ventana_principal.show()
        