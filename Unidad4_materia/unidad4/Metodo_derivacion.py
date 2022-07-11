#hace el metodo de derivacion

import sympy as sp
import numpy as np

class Metodo_derivacion():

    def f(self,expresion, x):
        # evalua la expresion dada, en base al valor dado en x 
       
        resultado_evaluacion = eval(str(expresion))
        return resultado_evaluacion

    def derivar_expresion(self, expresion):

        # deriva la expresion
        x_simbolo = sp.symbols('x')#colocamos los simbolos

        return  str(sp.diff(expresion, x_simbolo))

    def proceso(self, expresion, valor_inicial_x, valor_h, iteraciones):
        # realiza el proceso de derivacion 
        
        h = valor_h
        h_decremento = valor_h*0.1

        # el eesultado que obtenemos de remplazar el valor inicial de x, en la expresion que nos dieron
        valor_remplazo_x = self.f(expresion,valor_inicial_x)

        # x aca seria la representacion de Xi+1
        x = 0

        # la expresion derivada asi como el valor real y la x inicial, nunca cambian es por eso que las calculamos
        # desde un inicio
    
        expresion_derivada = self.derivar_expresion(expresion)

        aproximacion = 0
        valor_real = self.f(expresion_derivada, valor_inicial_x)
        error = 100

        contador = 0

        resultados = []

        while(error > 0.01 and contador < iteraciones):

            x = valor_inicial_x + h
           
            valor_remplazo_x_nuevo =  self.f(expresion,x)
            aproximacion = ( valor_remplazo_x_nuevo - valor_remplazo_x   )/h
            error = np.abs( (valor_real - aproximacion)/valor_real )*100

            resultados.append( [h,valor_inicial_x, x, valor_remplazo_x, valor_remplazo_x_nuevo, aproximacion, valor_real, error] )

            #print("h:", h, ",Xi:", valor_inicial_x, ",Xi+1:", x, ",F(Xi):", valor_remplazo_x
            #        ,",f(Xi+1):", valor_remplazo_x_nuevo, ",aproximacion:", aproximacion,
            #       ",error:", error)

            h -= h_decremento
            h_decremento = h*0.5 # sirve para que el decremeto de h siempre sea la mitad del valor de la h

            contador+=1

        return resultados

            

        

        



if(__name__ == "__main__"):

    m = Metodo_derivacion()
    print(m.proceso("-0.1*x**4-0.15*x**3-0.5*x**2-0.25*x+1.2",0.5,0.25,100))





    