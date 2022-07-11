
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import LineString

from Unidad2_materia.metodosDeResolucionDeEcuaciones import metodoReduccion


class Igualacion_metodo(metodoReduccion.Reduccion_Metodo):

    def proceso_igualacion(self, valores_variables):

        #metodo de igualacion 
        x1 = valores_variables[0][0]
        y1 = valores_variables[0][1]
        resultado1 = valores_variables[0][2]

        
        x2 = valores_variables[1][0]
        y2 = valores_variables[1][1]
        resultado2 = valores_variables[1][2]

        #saber a cuanto equivale y en las dos ecuaciones
        remplazo_y1_parte1 = resultado1/y1
        remplazo_y1_parte2 = (x1*-1)/y1

        remplazo_y2_parte1 = resultado2/y2
        remplazo_y2_parte2 = (x2*-1)/y2


        #se iguala a y
        x_con_numero = remplazo_y1_parte2 +  (remplazo_y2_parte2*-1)
        numeros_solos = remplazo_y2_parte1 + (remplazo_y1_parte1*-1)

        #se redondea el resultado
        resultado_x = round((numeros_solos/ x_con_numero), 3)

        resultado_y = round((((x1*resultado_x*-1) + resultado1)/ y1), 3)

        return resultado_x, resultado_y




if(__name__ == "__main__"):

    obj = Igualacion_metodo()
    lista = []
    sentencia = input("Dame la ecuacion 1:")
    sentenci2 = input("Dame la ecuacion 2:")
    lista.append(obj.valores_ecuacion_buscar(sentencia))
    lista.append(obj.valores_ecuacion_buscar(sentenci2))
    print(obj.proceso_igualacion(lista))

