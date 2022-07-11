
import sympy as sp
import numpy as np
from sympy.plotting import plot
from matplotlib import style

class Interpolacion_newton():

    def establecer_nombre_a(self, numero_puntos):
        #estable el numero que le corresponde a la variable a que vamos hacer
        for i in range(numero_puntos):

            yield i


    def encontrar_valores_a(self, matriz, numero_puntos):
        #   encuentra los numeros que van a remplazar a la letra a0, a1, etc en la formula

        numero_columnas = numero_puntos + 1 
        # cuantas columnas se va a regresar en x
        contar_x = 1
        columna_x = 0
        #columna que tomara para obtener la parte de arriba de la division
        columna_fx = 1
        fila_inicio = 1

        valores_a = []


        valores_a.append(matriz[0][1])

        for j in range(2,numero_columnas):

            for i in range(fila_inicio, numero_puntos):

                matriz[i][j] = (matriz[i][columna_fx] - matriz[i-1][columna_fx])/ (matriz[i][columna_x] - matriz[i-contar_x][columna_x])

                if(i == fila_inicio):
                    valores_a.append(matriz[i][j])

                

            fila_inicio += 1
            columna_fx += 1
            contar_x += 1

        #print(matriz)

        return valores_a

    def crear_ecuacion(self, numero_puntos):
        # crea en string la ecuacion correspondiente de newton dependiendo del numero de puntos dados

        ecuacion = "a0"
        multiplicando = "*(x-x_0)"

        for i in range(1,numero_puntos):

            ecuacion += f"+ a{i}" + multiplicando

            multiplicando += f"*(x-x_{i})"

        #print(ecuacion)

        return ecuacion



    def encontra_ecuacion(self, matriz, numero_puntos):

        # hace el proceso de newto para sacar la ecuacion que representa a los puntos

        valores_a = self.encontrar_valores_a(matriz, numero_puntos)
        ecuacion = self.crear_ecuacion(numero_puntos)

        x = sp.symbols('x')

        simbolos_x = sp.symbols("x_:" + str(numero_puntos))
        simbolos_a = sp.symbols("a:" + str(numero_puntos))

        #crea un diccionario con el nombre del simbolo y asociado a este
        diccionario_simbolos_x = {f'x_{i}' : simbolos_x[i] for i in range(numero_puntos)}
        diccionario_simbolos_a = {f'a{i}' : simbolos_a[i] for i in range(numero_puntos)}

        #crea las variables con ayuda del diccionario y las establece en el ambito global
        locals().update(diccionario_simbolos_x)
        locals().update(diccionario_simbolos_a)

        for i in range(numero_puntos):

            locals()[f'x_{i}'] = matriz[i][0]
            locals()[f'a{i}'] = valores_a[i]

        #print(locals())
        ecuacion_resultado = eval(ecuacion)  
        ecuacion_simplificada = sp.simplify(ecuacion_resultado)

        return str(ecuacion_simplificada)

        


    def graficar_ecuacion(self, ecuacion):

        #grafica la ecuacion dada con sympy
        x = sp.symbols('x')

        style.use('ggplot')
        plot(ecuacion, (x,10,-10))

    def evaluacion(self, valor_x, ecuacion):
        #remplaza el valor de x en la ecuacion y da el valor de y
        x = sp.symbols('x')
        x = valor_x
        resulado = eval(ecuacion)

        return str(resulado)


if(__name__ == "__main__"):

    m = Interpolacion_newton()
    matriz = np.zeros((3,4))
    matriz[0][0] = 1
    matriz[0][1] = 2 
    matriz[1][0] = 0
    matriz[1][1] = 4
    matriz[2][0] = -3
    matriz[2][1] = -2

    print(matriz)

    e = m.encontra_ecuacion(matriz, 3)

    m.graficar_ecuacion(e)
   

    print(m.evaluacion(-0.5,str(e)))
    
    
       




