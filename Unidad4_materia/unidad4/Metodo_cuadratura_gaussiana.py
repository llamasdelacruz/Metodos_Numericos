import mpmath 
import sympy as sp
from sympy import E, sympify # esta importacion es para que sympy tenga la constante e

# es el metod de la cuadratura gaussiana, aca si necesitamos una funcion y los puntos necesarios

class Cuadratura_gauss():


    def proceso(self,a,b, expresion, numero_puntos):

        resultado = 0

        # declaramos los simbolos que seran utilizados mas adelante
        x_simbolo,t,a_simbolo,b_simbolo,e = sp.symbols("x t a b e")
        
        # la expresion a la que sera igual x
        x_igualacion = "((b-a)*t+a+b)/2"

        # el valor de dx segun la formula 
        dx = (b-a)/2

        # nos devuelve a lo que sera igual x, remplazando a y b en la expresion que esta en x_igualacion
        x = eval(x_igualacion)
        # remplaza en la expresion dada a lo que es igual x
        expresion_remplazo = str(eval(expresion))

        # constante de euler que tuvimos que establecerle el valor de manera manual
        e = mpmath.mp.e
        
        # como la cuadratura de gauss tiene definido cuanto vale c1,c0,cn y cuanto vale t dependiendo la cantida de puntos
        # lo unico que hacemos es colocarlos y evaluar la expresion respecto a los puntos y obtenemos el resultado
        if(numero_puntos == 2):

            t = -0.5773
            expresion_final1 =  eval(expresion_remplazo)
            t = 0.5773
            expresion_final2 = eval(expresion_remplazo)

            resultado = (expresion_final1+expresion_final2)*dx

        elif(numero_puntos == 3):

            t = 0.7745966692
            expresion_final1 =  eval(expresion_remplazo)*0.55555555556

            t = 0.0
            expresion_final2 = eval(expresion_remplazo)*0.88888888889

            t = -0.7745966692
            expresion_final3 = eval(expresion_remplazo)*0.55555555556


            resultado = (expresion_final1 + expresion_final2 + expresion_final3)*dx

        elif(numero_puntos == 4):

            t = 0.8611363116
            expresion_final1 =  eval(expresion_remplazo)*0.7438548451

            t = 0.3399810436
            expresion_final2 = eval(expresion_remplazo)*0.6521451549

            t = -0.3399810436
            expresion_final3 = eval(expresion_remplazo)*0.7438548451

            t = -0.8611363116
            expresion_final4 = eval(expresion_remplazo)*0.6521451549


            resultado = (expresion_final1 + expresion_final2 + expresion_final3 + expresion_final4)*dx

        elif(numero_puntos == 5):

            t = 0.9061798459
            expresion_final1 =  eval(expresion_remplazo)*0.2369268850

            t = 0.5384693101
            expresion_final2 = eval(expresion_remplazo)*0.4786286705

            t = 0.0
            expresion_final3 = eval(expresion_remplazo)*0.5688888889

            t = -0.5384693101
            expresion_final4 = eval(expresion_remplazo)*0.4786286705

            t = -0.9061798459
            expresion_final5 = eval(expresion_remplazo)*0.2369268850


            resultado = (expresion_final1 + expresion_final2 + expresion_final3 + expresion_final4+ expresion_final5)*dx

        
        
        
       
        return resultado       

   



if(__name__ == "__main__"):

    m = Cuadratura_gauss()
    m.proceso(1,1.5, "e**-x**2", 2)
    #m.proceso(0,0.8, "0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5",3)
