from numpy import diff
import sympy as sp


class Serie_Taylor():

    def proceso(self, n, x_inicial, ecuacion):

        xsimbolo = sp.symbols('x')

        x = x_inicial

        # representa a f(x0)
        f_0 = str(eval(ecuacion))
        ecuacion_derivada = str(sp.diff(ecuacion)) 

        f_x = f"{f_0}+({str(eval(ecuacion_derivada))})*(x-{x_inicial})"
        
        for i in range(2,n+1):

            ecuacion_derivada = str(sp.diff(ecuacion_derivada)) 
            ecuacion_evaluada = str(eval(ecuacion_derivada))
            factorial_actual = str(sp.factorial(i))
            parte_f_x = f"+({ecuacion_evaluada}*(x-{x_inicial})**{i})/{factorial_actual}"

            f_x += parte_f_x

        return f_x
      

            



        



if(__name__=="__main__"):

    m = Serie_Taylor()
    print(m.proceso(3,0,"-x**3-0.1*x**2-0.15*x+1"))