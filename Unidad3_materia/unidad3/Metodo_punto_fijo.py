import numpy as np
import sympy as sp
from sympy import pprint


class Punto_fijo():

    #para que funcione, las dos ecuaciones que se le deben de pasar ya deben estar despejadas,
    #asi el programa solo hace el remplazo

    def proceso_punto_fijo(self, expresion1, expresion2, xentrada, yentrada, iteraciones):

        simbolox, simboloy = sp.symbols('x y')

        x = xentrada
        y = yentrada

        resultados = []

        

        for i in range(iteraciones):
            

            #print("{:.4f}".format(x),"{:.4f}".format(y))


            resultados.append([x,y])

            xnueva = eval(expresion1)

            x = xnueva

            ynueva = eval(expresion2)

            
            y = ynueva

            
        return resultados



if(__name__ == "__main__"):

    m = Punto_fijo()
    m.proceso_punto_fijo("(10-(x*y))**(1/2)", "((57-y)/(3*x))**(1/2)", 1.5,3.5, 3)


            


