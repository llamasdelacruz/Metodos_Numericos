import numpy as np

class Metodos_minimos_cuadrados():

    def calcular_datos(self,matriz, numero_datos):
        #calcuyula la sumatoria de x, y, xy, x^2

        x_sumatoria = 0
        y_sumatoria = 0
        xy_sumatoria = 0
        x_cuadrada_sumatoria = 0

        for i in range(numero_datos):

            x_sumatoria += matriz[i][0]
            y_sumatoria += matriz[i][1]

            xy_sumatoria += matriz[i][0]*matriz[i][1]

            x_cuadrada_sumatoria += matriz[i][0]**2

        return x_sumatoria, y_sumatoria, xy_sumatoria, x_cuadrada_sumatoria


    def calcular_ecuacion(self, x_sumatoria, y_sumatoria, xy_sumatoria, x_cuadrada_sumatoria, numero_datos):
        # calcula la ecuacion de la recta y = mx + b

        m = (xy_sumatoria-((x_sumatoria*y_sumatoria)/numero_datos))/(x_cuadrada_sumatoria-((x_sumatoria**2)/numero_datos))
        b = (y_sumatoria/numero_datos)-(m*(x_sumatoria/numero_datos))

        ecuacion = f"{m}*x+{b}"

        return ecuacion

    def proceso(self, matriz, numero_datos):
        #hace el proces de minimos cuadrados 

        x_sumatoria, y_sumatoria, xy_sumatoria, x_cuadrada_sumatoria = self.calcular_datos(matriz, numero_datos)
        ecuacion = self.calcular_ecuacion( x_sumatoria, y_sumatoria, xy_sumatoria, x_cuadrada_sumatoria, numero_datos)
        
        return ecuacion

if(__name__ == "__main__"):
    #caliz
    m = Metodos_minimos_cuadrados()
    matriz = np.zeros((9,2))
    matriz[0][0] = 7
    matriz[1][0] = 1
    matriz[2][0] = 10
    matriz[3][0] = 5
    matriz[4][0] = 4
    matriz[5][0] = 3
    matriz[6][0] = 13
    matriz[7][0] = 10
    matriz[8][0] = 2

    matriz[0][1] = 2
    matriz[1][1] = 9
    matriz[2][1] = 2
    matriz[3][1] = 5
    matriz[4][1] = 7
    matriz[5][1] = 11
    matriz[6][1] = 2
    matriz[7][1] = 5
    matriz[8][1] = 14


    m.proceso(matriz,9)