import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont #fuentes
import ctypes #getSystemMetrico
import numpy as np

#codigo fabricado
from Unidad2_materia.metodos_intervalo.metodo_biseccion import Biseccion_metodo
from Unidad2_materia.metodos_intervalo.metodo_aproximaciones_sucesivas import Aproximaciones_sucesivas
from Unidad2_materia.metodos_intervalo.metodo_interpolacion import Interpolacion

from Unidad2_materia.metodos_intervalo.metodo_grafico_intervalo import Intervalo_grafico_metodo

class Ventana_intervalos(QMainWindow):

    def __init__(self, ventana_principal):

        self.ventana_principal = ventana_principal

        QMainWindow.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("Unidad2_materia/Ventana_metodos_intervalo.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)

        self.biseccion.clicked.connect(self.biseccion_metodo)
        self.puntoFijo.clicked.connect(self.aproximaciones_sucesivas_metodo)
        self.interpolacion.clicked.connect(self.interpolacion_metodo)
        self.grafico.clicked.connect(self.grafico_metodo)


    def biseccion_metodo(self):

        if(self.comboBox.currentIndex() == 0 and self.primera1.text() != "" and self.primera2.text() != "" and self.primera3.text() != "" and self.primera4.text() != "" and self.primera5.text() != ""):

            lista_datos = [self.primera1.text(), self.primera2.text(), self.primera3.text(), self.primera4.text(), self.primera5.text()]
            lista_datos_flotantes = list(np.float_(lista_datos))

            tolerancia = float(self.tolerancia.text())
            xl = float(self.xl.text())
            xu = float(self.xu.text())

            obj = Biseccion_metodo( lista_datos_flotantes, 1)
            self.Resultado.setText("Bisección: "+str(obj.encontrar_raiz(xl,xu, tolerancia)))
            self.Resultado.adjustSize()
            
        elif(self.comboBox.currentIndex() == 1):

            tolerancia = float(self.tolerancia.text())
            xl = float(self.xl.text())
            xu = float(self.xu.text())

            lista_datos = [self.segunda1.text(), self.segunda2.text(), self.segunda3.text(), self.segunda4.text()]
            lista_datos_flotantes = list(np.float_(lista_datos))

            obj = Biseccion_metodo( lista_datos_flotantes, 2)
            
            self.Resultado.setText("Bisección: "+str(obj.encontrar_raiz(xl,xu, tolerancia)))
            self.Resultado.adjustSize()

        elif(self.comboBox.currentIndex() == 2):

            lista_datos = [self.tercera1.text(), self.tercera2.text(), self.tercera3.text(), self.tercera4.text(), self.tercera5.text(), self.tercera6.text() ]
            lista_datos_flotantes = list(np.float_(lista_datos))

            tolerancia = float(self.tolerancia.text())
            xl = float(self.xl.text())
            xu = float(self.xu.text())

            obj = Biseccion_metodo( lista_datos_flotantes, 3)
            
            self.Resultado.setText("Bisección: "+str(obj.encontrar_raiz(xl,xu, tolerancia)))
            self.Resultado.adjustSize()

        elif(self.comboBox.currentIndex() == 3):

            lista_datos = [self.cuarta1.text(), self.cuarta2.text()]
            lista_datos_flotantes = list(np.float_(lista_datos))

            tolerancia = float(self.tolerancia.text())
            xl = float(self.xl.text())
            xu = float(self.xu.text())

            obj = Biseccion_metodo( lista_datos_flotantes, 4)
            self.Resultado.setText("Bisección: "+str(obj.encontrar_raiz(xl,xu, tolerancia)))
            self.Resultado.adjustSize()

        elif(self.comboBox.currentIndex() == 4):

            lista_datos = [self.quinta1.text(), self.quinta2.text()]
            lista_datos_flotantes = list(np.float_(lista_datos))

            tolerancia = float(self.tolerancia.text())
            xl = float(self.xl.text())
            xu = float(self.xu.text())

            obj = Biseccion_metodo( lista_datos_flotantes, 5)
           
            self.Resultado.setText("Bisección: "+str(obj.encontrar_raiz(xl,xu, tolerancia)))
            self.Resultado.adjustSize()

    def aproximaciones_sucesivas_metodo(self):

        if(self.comboBox.currentIndex() == 0):

            lista_datos = [self.primera1.text(), self.primera2.text(), self.primera3.text(), self.primera4.text(), self.primera5.text()]
            lista_datos_flotantes = list(np.float_(lista_datos))

            tolerancia = float(self.tolerancia.text())
            

            obj = Aproximaciones_sucesivas(lista_datos_flotantes, 1)
            self.Resultado.setText( "Punto fijo: "+ str(obj.ciclo(tolerancia)))

            self.Resultado.adjustSize()
            

        elif(self.comboBox.currentIndex() == 1):

            lista_datos = [self.segunda1.text(), self.segunda2.text(), self.segunda3.text(), self.segunda4.text()]
            lista_datos_flotantes = list(np.float_(lista_datos))

            tolerancia = float(self.tolerancia.text())
        

            obj = Aproximaciones_sucesivas(lista_datos_flotantes, 2)
            self.Resultado.setText("Punto fijo: " + str(obj.ciclo(tolerancia)))

            self.Resultado.adjustSize()
            
        elif(self.comboBox.currentIndex() == 2):

            lista_datos = [self.tercera1.text(), self.tercera2.text(), self.tercera3.text(), self.tercera4.text(), self.tercera5.text(), self.tercera6.text() ]
            lista_datos_flotantes = list(np.float_(lista_datos))

            tolerancia = float(self.tolerancia.text())
        

            obj = Aproximaciones_sucesivas(lista_datos_flotantes, 3)
            self.Resultado.setText("Punto fijo: "+ str(obj.ciclo(tolerancia)))

            self.Resultado.adjustSize()

        elif(self.comboBox.currentIndex() == 3):

            lista_datos = [self.cuarta1.text(), self.cuarta2.text()]
            lista_datos_flotantes = list(np.float_(lista_datos))

            tolerancia = float(self.tolerancia.text())
        

            obj = Aproximaciones_sucesivas(lista_datos_flotantes, 4)
            self.Resultado.setText("Punto fijo: " + str(obj.ciclo(tolerancia)))

            self.Resultado.adjustSize()


        elif(self.comboBox.currentIndex() == 4):

            lista_datos = [self.quinta1.text(), self.quinta2.text()]
            lista_datos_flotantes = list(np.float_(lista_datos))

            tolerancia = float(self.tolerancia.text())
        

            obj = Aproximaciones_sucesivas(lista_datos_flotantes, 5)
            self.Resultado.setText("Punto fijo: " + str(obj.ciclo(tolerancia)))

            self.Resultado.adjustSize()



           
    def interpolacion_metodo(self):

        if(self.comboBox.currentIndex() == 0):

            lista_datos = [self.primera1.text(), self.primera2.text(), self.primera3.text(), self.primera4.text(), self.primera5.text()]
            lista_datos_flotantes = list(np.float_(lista_datos))

            tolerancia = float(self.tolerancia.text())
            xl = float(self.xl.text())
            xu = float(self.xu.text())

            obj = Interpolacion(lista_datos_flotantes, 1)
            
            self.Resultado.setText("Interpolacion:"+str(obj.encontrar_raiz(xl,xu,tolerancia)))
            self.Resultado.adjustSize()
            

        elif(self.comboBox.currentIndex() == 1):

            lista_datos = [self.segunda1.text(), self.segunda2.text(), self.segunda3.text(), self.segunda4.text()]
            lista_datos_flotantes = list(np.float_(lista_datos))

            tolerancia = float(self.tolerancia.text())
            xl = float(self.xl.text())
            xu = float(self.xu.text())

            obj = Interpolacion(lista_datos_flotantes, 2)
            
            self.Resultado.setText("Interpolacion:"+str(obj.encontrar_raiz(xl,xu,tolerancia)))
           

            self.Resultado.adjustSize()
            
        elif(self.comboBox.currentIndex() == 2):

            lista_datos = [self.tercera1.text(), self.tercera2.text(), self.tercera3.text(), self.tercera4.text(), self.tercera5.text(), self.tercera6.text() ]
            lista_datos_flotantes = list(np.float_(lista_datos))

            tolerancia = float(self.tolerancia.text())
            xl = float(self.xl.text())
            xu = float(self.xu.text())

            obj = Interpolacion(lista_datos_flotantes, 3)
            
            self.Resultado.setText("Interpolacion:"+str(obj.encontrar_raiz(xl,xu,tolerancia)))


            self.Resultado.adjustSize()

        elif(self.comboBox.currentIndex() == 3):

            lista_datos = [self.cuarta1.text(), self.cuarta2.text()]
            lista_datos_flotantes = list(np.float_(lista_datos))

            tolerancia = float(self.tolerancia.text())
            xl = float(self.xl.text())
            xu = float(self.xu.text())

            obj = Interpolacion(lista_datos_flotantes, 4)
            
            self.Resultado.setText("Interpolacion:"+str(obj.encontrar_raiz(xl,xu,tolerancia)))


            self.Resultado.adjustSize()

        elif(self.comboBox.currentIndex() == 4):

            lista_datos = [self.quinta1.text(), self.quinta2.text()]
            lista_datos_flotantes = list(np.float_(lista_datos))

            tolerancia = float(self.tolerancia.text())
            xl = float(self.xl.text())
            xu = float(self.xu.text())

            obj = Interpolacion(lista_datos_flotantes, 5)
            
            self.Resultado.setText("Interpolacion:"+str(obj.encontrar_raiz(xl,xu,tolerancia)))


            self.Resultado.adjustSize()

    def grafico_metodo(self):

        if(self.comboBox.currentIndex() == 0):

            lista_datos = [self.primera1.text(), self.primera2.text(), self.primera3.text(), self.primera4.text(), self.primera5.text()]
            lista_datos_flotantes = list(np.float_(lista_datos))

            obj = Intervalo_grafico_metodo(lista_datos_flotantes, 1)
            self.Resultado.setText("Gráfico:"+str(obj.graficar()))
            
            self.Resultado.adjustSize()
            

        elif(self.comboBox.currentIndex() == 1):

            lista_datos = [self.segunda1.text(), self.segunda2.text(), self.segunda3.text(), self.segunda4.text()]
            lista_datos_flotantes = list(np.float_(lista_datos))

            obj = Intervalo_grafico_metodo(lista_datos_flotantes, 2)
            self.Resultado.setText("Gráfico:"+str(obj.graficar()))
           

            self.Resultado.adjustSize()
            
        elif(self.comboBox.currentIndex() == 2):

            lista_datos = [self.tercera1.text(), self.tercera2.text(), self.tercera3.text(), self.tercera4.text(), self.tercera5.text(), self.tercera6.text() ]
            lista_datos_flotantes = list(np.float_(lista_datos))

            obj = Intervalo_grafico_metodo(lista_datos_flotantes, 3)
            self.Resultado.setText("Gráfico:"+str(obj.graficar()))
           

            self.Resultado.adjustSize()


        elif(self.comboBox.currentIndex() == 3):

            lista_datos = [self.cuarta1.text(), self.cuarta2.text()]
            lista_datos_flotantes = list(np.float_(lista_datos))

            obj = Intervalo_grafico_metodo(lista_datos_flotantes, 4)
            self.Resultado.setText("Gráfico:"+str(obj.graficar()))
           

            self.Resultado.adjustSize()

        elif(self.comboBox.currentIndex() == 4):

            lista_datos = [self.quinta1.text(), self.quinta2.text()]
            lista_datos_flotantes = list(np.float_(lista_datos))

            obj = Intervalo_grafico_metodo(lista_datos_flotantes, 5)
            self.Resultado.setText("Gráfico:"+str(obj.graficar()))
           

            self.Resultado.adjustSize()



        



    def closeEvent(self, event):

        self.ventana_principal.show()
        
