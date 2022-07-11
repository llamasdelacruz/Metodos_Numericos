

#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import LineString
from Unidad2_materia.metodos_intervalo.metodo_biseccion import Biseccion_metodo


class Intervalo_grafico_metodo(Biseccion_metodo):

    def __init__(self, multiplican, numero_funcion):

        self.multiplican = multiplican
        self.numero_ecuacion = numero_funcion


    def graficar(self):
        """    
        linea_x = np.arange(-5,5)

        linea_ecuacion1_y = [ self.practica_funcion(i) for i in range(-5, 5)]
        linea_ecuacion2_y = [0] * 10

        plt.plot(linea_x, linea_ecuacion1_y)
        plt.plot(linea_x, linea_ecuacion2_y)

        first_line = LineString(np.column_stack((linea_x, linea_ecuacion1_y)))
        second_line = LineString(np.column_stack((linea_x, linea_ecuacion2_y)))
        intersection = second_line.intersection(first_line)

        if intersection.geom_type == 'MultiPoint':
            plt.plot(*LineString(intersection).xy, 'o')
        elif intersection.geom_type == 'Point':
            plt.plot(*intersection.xy, 'o')

        #regresa las cordenadas del punto en que se conectan 
        x, y = intersection.xy
        plt.title("x = {}, y = {}".format(x[0],y[0]))
        plt.grid()
        plt.show()"""
        
        x = np.linspace(-1000,2, 1000)
        y = np.zeros(1000)
        
        
        plt.plot(x,self.practica_funcion(x))
        plt.plot(x, y)

        first_line = LineString(np.column_stack((x,self.practica_funcion(x))))
        second_line = LineString(np.column_stack((x, y)))
        intersection = second_line.intersection(first_line)

        if intersection.geom_type == 'MultiPoint':
            plt.plot(*LineString(intersection).xy, 'o')
        elif intersection.geom_type == 'Point':
            plt.plot(*intersection.xy, 'o')

        #regresa las cordenadas del punto en que se conectan 
        x, y = intersection.xy
        plt.title("x = {}, y = {}".format(x[0],y[0]))
        plt.grid()
        plt.show()


        return x[0]




if(__name__ == "__main__"):

    objeto  = Intervalo_grafico_metodo(-1, 1)

    print(objeto.graficar())





