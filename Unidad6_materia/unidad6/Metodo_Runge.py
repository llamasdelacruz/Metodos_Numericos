import sympy as sp

class Metodo_Runge_cuarto_grado():

    def proceso(self, x_inicial, y_inicial, ecuacion, h, x_tope):
        # realiza el proceso de runge-kutta de cuarto orden
        resultados = []
        x_simbolo, y_simbolo = sp.symbols('x y')
        xi = x_inicial
        yi = y_inicial

        while(xi < x_tope):

            x = xi # estas variables de x y y debemos re declararlas con un valor para que el programa pueda remplazarlos en la ecuacion
            y = yi

            k1 = eval(ecuacion)
            #print("k1:",k1)
            

            x = xi+(h/2) 
            y = yi+k1*h/2
            k2 = eval(ecuacion)
            #print("k2:",k2)

            x = xi+(h/2) 
            y = yi+k2*h/2
            k3 = eval(ecuacion)
            #print("k3:",k3)

            x = xi+h 
            y = yi+k3*h
            k4 = eval(ecuacion)
            #print("k4:",k4)
            yi_mas_uno = yi +(1/6)*(k1+2*k2 + 2*k3+k4)*h
            resultados.append([xi,yi,k1,k2,k3,k4,yi_mas_uno])
            yi = yi_mas_uno
            xi += h
            #print("yi:",yi, "xi:",xi)


        return resultados  



if(__name__== "__main__"):

    m = Metodo_Runge_cuarto_grado()
    m.proceso(1,4,"x*(y**(1/2))",0.2, 1.6)