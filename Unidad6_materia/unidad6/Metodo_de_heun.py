import sympy as sp
import numpy as np
import mpmath 

class Metodo_de_Heun():

    #realiza el metodo de heun

    def proceso(self,h,x_inicial,x_final,y_inicio, ecuacion, error_minimo):

        # declara los simbolos para que los lea sympy
        xsimbolo, ysimbolo, e = sp.symbols('x y e')
        e = mpmath.mp.e #establecemos el valor de e

        error = 100 # para que entre al bucle establecemos el error commo 100
        #damos valores iniciales a la siguientes variables
        # pues estos solo seran dados uno vez
        xi = x_inicial
        yi = y_inicio

        x = xi
        y = yi

        evaluacion_fxy = eval(ecuacion)
        yi_mas_diez = y+evaluacion_fxy*h

        resultados = []
       
        while(xi <= x_final):

            while(error> error_minimo):
                #este ciclo sigue la solucion normal iterativo de la froma de Heun
                x = xi
                y = yi

                evaluacion_fxy = eval(ecuacion)

                xi_mas_uno = x + h
                x = xi_mas_uno

                y = yi_mas_diez 
                
                evaluacion_fxiyi = eval(ecuacion)

                yi_mas_uno =  yi+((evaluacion_fxy+evaluacion_fxiyi)/2*h)

                error = np.abs((yi_mas_uno-yi_mas_diez)/yi_mas_uno)*100

                #print(f"xi:{xi}, yi:{yi},f(xi,yi):{evaluacion_fxy}, xi+1:{xi_mas_uno}, yi+10:{yi_mas_diez}, f(xi+1,yi+10):{evaluacion_fxiyi}, yi+1:{yi_mas_uno}, error:{error}")
                resultados.append([xi,yi,evaluacion_fxy,xi_mas_uno,yi_mas_diez,evaluacion_fxiyi,yi_mas_uno,error])
                yi_mas_diez = yi_mas_uno

            # los mismos valores que les dimos un valor inicial, les cambiamos los valores
            xi = xi_mas_uno
            yi = yi_mas_uno

            x = xi
            y = yi

            evaluacion_fxy = eval(ecuacion)
            # como yi_mas_diez es igual a yi^0, esta requiere de ser inicializada con una formula
            # despues su valor se iguala a yi_mas_uno, para que al final cuando el erro sea menor al errro minimo establecido
            # vuelva a calcularse su valor con la misma formula
            yi_mas_diez = y+evaluacion_fxy*h 
            
            error = 100

        return resultados

if(__name__== "__main__"):
    m = Metodo_de_Heun()
    print(m.proceso(1,0,4,2,"4*(e**(0.8*x))-0.5*y",0.1))