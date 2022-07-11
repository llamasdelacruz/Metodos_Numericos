import sympy as sp
# este resuelve el metodo d euler

class Metodo_Euler():

    def proceso_euler(self, valorx, valory, valorh, ecuacion, iteraciones):

        xsimbolo = sp.symbols('x')

        x = valorx
        y = valory
    
        h = valorh

        # nos regresa el valor de remplazar la x en la expresion
        evaluacion_ecuacion = eval(ecuacion)

        yi = y+(h*evaluacion_ecuacion)

        contador = 0

        resultados = []

        while(contador < iteraciones):

            #print(f"h:{h}, x:{x}, y:{y}, evaluacion:{evaluacion_ecuacion}, yi:{yi}")
            resultados.append([x,y,evaluacion_ecuacion, yi])
            y = yi
            x += h

            evaluacion_ecuacion = eval(ecuacion)

            yi = y+(h*evaluacion_ecuacion)

            contador +=1

        return resultados



if(__name__=="__main__"):
    m = Metodo_Euler()
    print(m.proceso_euler(0,1,0.5, "-2*x**3+12*x**2-20*x+8.5", 10))




        





    
