
#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib .pyplot as plt
from Unidad2_materia.metodos_intervalo.metodo_biseccion import Biseccion_metodo

class Aproximaciones_sucesivas(Biseccion_metodo):

    def __init__(self, multiplican, numero_funcion):
        # esto de aqui sirve para poder indicar que ecuacion vamoa a utilizar en el programa
        self.multiplican = multiplican
        self.numero_ecuacion = numero_funcion



    def ciclo(self, tolerancia):

        Tolerancia = tolerancia
        xi = 0
        Error = np.abs(self.gx(xi)-xi)
        i = 0

        while(Error > Tolerancia and i <= 10000):
            
            if(i>0):
                
                Error = np.abs(self.gx(xi)-xi)
                
            xi = self.gx(xi)
            i = i + 1
        #print(xi)

        x = np.linspace(0,1.5, 1000)
        plt.title("Metodo del punto fijo ")
        plt.plot(x, self.practica_funcion(x), label="f(x)")
        plt.plot(x,self.gx(x), label = "g(x)")
        plt.plot(x,x,label = "f(x) = x")
        plt.axvline(xi, label="f(x) = 0, x = (xi: .6f)", color = "k")
        plt.axhline(0, color = "k")
        plt.legend(loc='upper right')

        plt.grid()
        plt.show()
        return xi