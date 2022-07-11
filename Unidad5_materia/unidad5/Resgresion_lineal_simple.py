import numpy as np

class Regresion_lineal():

    def calcular_datos(self, matriz, numero_datos):
        # calcula el x^2, x*y, y**2 y su sumatoria
        x_promedio = 0
        y_promedio = 0
        x_cuadrada_sumatoria = 0
        xy_sumatoria = 0
        y_cuadrada_sumatoria = 0
        y_sumatoria = 0


        for i in range(numero_datos):


            x_promedio += matriz[i][0]
            y_sumatoria += matriz[i][1]

            x_cuadrada_sumatoria += matriz[i][0]**2
            y_cuadrada_sumatoria += matriz[i][1]**2

            xy_sumatoria += matriz[i][0]*matriz[i][1]


        x_promedio = x_promedio/numero_datos
        y_promedio = y_sumatoria/numero_datos

        #print(x_promedio, y_promedio, x_cuadrada_sumatoria, y_cuadrada_sumatoria,  xy_sumatoria, y_sumatoria)
        return x_promedio, y_promedio, x_cuadrada_sumatoria, y_cuadrada_sumatoria,  xy_sumatoria, y_sumatoria

    def calcular_ecuacion(self, x_promedio, y_promedio, x_cuadrada_sumatoria,  xy_sumatoria, numero_datos):
        #calcula el la ecuacion y-bx con los valores dados

        b = (xy_sumatoria -(numero_datos*x_promedio*y_promedio))/(x_cuadrada_sumatoria-(numero_datos*(x_promedio**2)))        
        a =  y_promedio -(b*x_promedio)
        
        ecuacion = f"{a}+{b}*x"

        return ecuacion, a, b
        
    def error_regresion_lineal(self, a,b, y_cuadrada_sumatoria, y_sumatoria, xy_sumatoria, numero_datos):
        # calcula el error estandar de la estimacion 

        error = ((y_cuadrada_sumatoria-(a*y_sumatoria)-(b*xy_sumatoria))/(numero_datos-2))**(1/2)
        
        return error

    def proceso_regresion(self,matriz, numero_datos):
        # realiza el armado de los procesos necesarios
        # para la obtencion de la ecuacion y el error de 
        # la regresion lineal

        x_promedio, y_promedio, x_cuadrada_sumatoria, y_cuadrada_sumatoria,  xy_sumatoria, y_sumatoria = self.calcular_datos(matriz, numero_datos)
        ecuacion, a, b = self.calcular_ecuacion(x_promedio, y_promedio, x_cuadrada_sumatoria, xy_sumatoria, numero_datos)
        error = self.error_regresion_lineal(a,b, y_cuadrada_sumatoria, y_sumatoria, xy_sumatoria, numero_datos)
       
        return ecuacion, error


if(__name__ == "__main__"):
    #caliz
    m = Regresion_lineal()
    matriz = np.zeros((6,2))
    matriz[0][0] = 1
    matriz[1][0] = 3
    matriz[2][0] = 4
    matriz[3][0] = 2
    matriz[4][0] = 1
    matriz[5][0] = 7

    matriz[0][1] = 2
    matriz[1][1] = 3
    matriz[2][1] = 2.5
    matriz[3][1] = 2
    matriz[4][1] = 2
    matriz[5][1] = 3.5


    m.proceso_regresion(matriz, 6)
   