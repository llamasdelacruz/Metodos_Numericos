
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import LineString

from Unidad2_materia.metodosDeResolucionDeEcuaciones import metodoReduccion


class Grafico_metodo(metodoReduccion.Reduccion_Metodo):


    def grafica(self, valores_variables):
        #coloca las lineas y encuentra la interseccion
        y1 = valores_variables[0][1]

        x1 = (valores_variables[0][0] * -1)/y1
        
        resultado1 = valores_variables[0][2]/y1


        y2 = valores_variables[1][1]
        x2 = (valores_variables[1][0] * -1)/y2
        
        resultado2 = (valores_variables[1][2])/y2

        linea_x = np.arange(-100,100)
        linea_ecuacion1_y = [ (i*x1) + resultado1 for i in range(-100, 100)]
        linea_ecuacion2_y = [ (i*x2) + resultado2 for i in range(-100, 100)]

        plt.plot(linea_x, linea_ecuacion1_y)
        plt.plot(linea_x, linea_ecuacion2_y)

        first_line = LineString(np.column_stack((linea_x, linea_ecuacion1_y)))
        second_line = LineString(np.column_stack((linea_x, linea_ecuacion2_y)))
        intersection = first_line.intersection(second_line)

        if intersection.geom_type == 'MultiPoint':
            plt.plot(*LineString(intersection).xy, 'o')
        elif intersection.geom_type == 'Point':
            plt.plot(*intersection.xy, 'o')

        #regresa las cordenadas del punto en que se conectan 
        x, y = intersection.xy
        
        plt.grid()
        plt.title("x = {}, y = {}".format(x[0],y[0]))
        plt.show()





if(__name__ == "__main__"):

    obj = Grafico_metodo()
    lista = []
    sentencia = input("Dame la ecuacion 1:")
    sentenci2 = input("Dame la ecuacion 2:")
    lista.append(obj.valores_ecuacion_buscar(sentencia))
    lista.append(obj.valores_ecuacion_buscar(sentenci2))
    obj.grafica(lista)