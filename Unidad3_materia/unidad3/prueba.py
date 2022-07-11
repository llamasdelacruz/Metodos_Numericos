from tkinter import Variable
import sympy as sp
import numpy as np





x,y,z,w,sin,cos,tan,cot,sec,csc,asin,acos,atan,acot,asec,acsc = sp.symbols('x y z w sin cos tan cot sec csc asin acos atan acot asec acsc')
def funcion2(x,y):
    texto = "x**2+3*y"

    expr = texto
    a = eval(expr)

    x1,y1 = sp.symbols('x y')

    derivada_x = sp.diff(expr,x1)
    print("Primera derivada: ",derivada_x)

    derivada_y = sp.diff(expr,y1)
    print("Segunda derivada: ",derivada_y)

    deri1 = eval(str(derivada_x))
    print("Valor del primer resultado derivado:",deri1)

    deri2 =eval(str(derivada_y))
    print("Valor del segundo resultado derivado: ", deri2)
    
    return a

a = funcion2(1,2)
print("El valor de a es: ", a)