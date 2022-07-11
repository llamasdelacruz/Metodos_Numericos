import sympy as sp
import numpy as np
from sympy.plotting import plot
from matplotlib import style

class Interpolacion_lagrange():


    def proceso_lagrange(self, puntos, cantidad):


        x = sp.symbols('x')

        simbolos = sp.symbols("x_:" + str(cantidad))
        simbolos2 = sp.symbols("f_:" + str(cantidad))
        simbolos3 = sp.symbols("l_:" + str(cantidad))

        #crea un diccionario con el nombre del simbolo y asociado a este
        diccionario_simbolos1 = {f'x_{i}' : simbolos[i] for i in range(cantidad)}
        diccionario_simbolos2 = {f'f_{i}' : simbolos2[i] for i in range(cantidad)}
        diccionario_simbolos3 = {f'l_{i}' : simbolos3[i] for i in range(cantidad)}

        #crea las variables con ayuda del diccionario y las establece en el ambito global
        locals().update(diccionario_simbolos1)
        locals().update(diccionario_simbolos2)
        locals().update(diccionario_simbolos3)


        for i in range(cantidad):

            locals()[f'x_{i}'] = puntos[i][0]
            locals()[f'f_{i}'] = puntos[i][1]


        #print(locals())
        
        for i in range(cantidad):

            expresion_arriba = ""
            expresion_abajo = ""

            for j in range(cantidad):

                if(j != i):

                    if(not expresion_arriba):

                        expresion_arriba = f"(x-x_{j})"
                        expresion_abajo = f"(x_{i}-x_{j})"
                    else:

                        expresion_arriba += f"*(x-x_{j})"
                        expresion_abajo += f"*(x_{i}-x_{j})"

            total = expresion_arriba +"/(" + expresion_abajo + ")"

    
            locals()[f'l_{i}'] = eval(total)

            #print(locals()[f'l_{i}'])
        expresion = ""
        for i in range(cantidad):


            if(not expresion):

                expresion = f"(f_{i}*l_{i})"

            else:

                expresion += f"+(f_{i}*l_{i})"

        resultado = eval(expresion)
        ecuacion_simplificada = sp.simplify(resultado)
        
        return str(ecuacion_simplificada)


if(__name__ == "__main__"):

    m = Interpolacion_lagrange()
    matriz = np.zeros((3,2))
    

    matriz[0][0] = 0
    matriz[0][1] = 1
    matriz[1][0] = 1
    matriz[1][1] = 3
    matriz[2][0] = 2
    matriz[2][1] = 0

    #print(matriz)

    m.proceso_lagrange(matriz, 3)
    #m.proceso_lagrange([[-1,15],[4,5],[5,9]], 3)
    #m.proceso_lagrange([[0,1],[1,3],[2,0]],3)

    
