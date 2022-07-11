
#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import pandas as pd

import numpy as np
from Unidad2_materia.metodosDeResolucionDeEcuaciones import metodoReduccion 

class Sustitucion_metodo(metodoReduccion.Reduccion_Metodo):

    def proceso_sustitucion(self, valores_variables):
        #se usa el metodo de sustitucion para resolver esta ecuaciones lineales
        x1 = valores_variables[0][0]
        y1 = valores_variables[0][1]
        resultado1 = valores_variables[0][2]

        
        x2 = valores_variables[1][0]
        y2 = valores_variables[1][1]
        resultado2 = valores_variables[1][2]


        #Saber a que es equivalente y para remplazarla
        remplazo_y_parte1 = resultado1/y1
        remplazo_y_parte2 = (x1*-1)/y1

        remplazo_y_parte1 *= y2
        remplazo_y_parte2 *= y2

        x2 += remplazo_y_parte2

        resultado_x = round(((remplazo_y_parte1*-1)+resultado2)/x2, 3)

        #remplazar el valor real de x en la primera ecuacion

        x1 *= resultado_x

        resultado_y = round((resultado1 + (x1*-1))/y1, 3)

        return resultado_x, resultado_y

        


if(__name__ == "__main__"):

    obj = Sustitucion_metodo()
    lista = []
    sentencia = input("Dame la ecuacion 1:")
    sentenci2 = input("Dame la ecuacion 2:")
    lista.append(obj.valores_ecuacion_buscar(sentencia))
    lista.append(obj.valores_ecuacion_buscar(sentenci2))
    print(obj.proceso_sustitucion(lista))

