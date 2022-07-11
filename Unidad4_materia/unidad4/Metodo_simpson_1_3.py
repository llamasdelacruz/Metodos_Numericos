
import numpy as np
import sympy as sp


class Metodo_simpson_1_3():

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
        #realiza el proceso de de integracion de metodo simpson 1/3

        resultados = []

        # tamaño de paso
        h = (valor_b - valor_a)/2
        
        X0 = valor_a
        X1 = X0 + h
        X2 = valor_b

        f_X0 = self.f(expresion,X0)
        f_X1 = self.f(expresion,X1)
        f_X2 = self.f(expresion, X2)

        aproximacion = (h/3)* (f_X0 + 4*f_X1 + f_X2)


        valor_real = self.integral_expresion(expresion, valor_a, valor_b)

        error = (valor_real - aproximacion)/valor_real * 100

        resultados.append(valor_real)
        resultados.append(aproximacion)
        resultados.append(error)

        return resultados
        

if __name__ == "__main__":

    m = Metodo_simpson_1_3()
    print(m.proceso("0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5", 0,0.8))