
import numpy as np
import sympy as sp


class Metodo_integracion_trapecios():

    def f(self,expresion, x):
        # evalua la expresion dada, en base al valor dado en x 
       
        resultado_evaluacion = eval(expresion)

        return resultado_evaluacion

    def integral_expresion(self, expresion, a,b):
        #realiza la integral evaluada en los limites dados
        x_simbolo,a_simbolo,b_simbolo = sp.symbols("x a b")

        # con integrate, integramos la expresion, por medio de una tupla
        # pasamos respecto a cual simbolo se esta integrando y los limites
        # de integracion, el evalf, nos sirve para que despues de que integre la expresion
        # nos de un resultado numerico, y no el resultado en forma de una expresion
        # en evalf(6), le colocamos el 6 entre parentesis porque es el numero de decimales 
        # que nos dara en el resultado

        integral_respecto_x = sp.integrate(expresion, (x_simbolo, a,b)).evalf(6)

        return integral_respecto_x


    
    def proceso(self, expresion,valor_a, valor_b):
        #realiza el proceso de de integracion de trapecios

        resultados = []

        f_a = self.f(expresion,valor_a)
        f_b = self.f(expresion, valor_b)

        aproximacion = (valor_b - valor_a)* ((f_a + f_b)/2)

        valor_real = self.integral_expresion(expresion, valor_a, valor_b)

        error = (valor_real - aproximacion)/valor_real * 100

        resultados.append(valor_real)
        resultados.append(aproximacion)
        resultados.append(error)

        return resultados
        




