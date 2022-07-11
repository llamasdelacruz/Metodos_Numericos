#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import re
import numpy as np


class Jacobi():


    def valores_ecuacion_buscar_expreciones_regulares(self, restriccion_sentencia):
        #toma la cadena y separa los valores con ayuda de las expresiones regulares
        #'\d+' \d es un dígito (un carácter en el rango 0-9), y + significa 1 o más veces. Así que, \d+ es de 1 o más dígitos. -?\d+\.?\d?

        #Fuente: https://www.iteramos.com/pregunta/99835/que-hace-d--significa-en-terminos-de-expresion-regular
        
        self.exprecion =  self.prepara_sentencia(restriccion_sentencia)
        self.bandera = False
        lista_valores = []
        try:
            #lista_valores = [float(s) for s in re.findall(r'\d+', self.exprecion)]

            lista_valores = [float(s) for s in re.findall(r'-?\d+\.?\d?', self.exprecion)]

        except:
            print("Error al introducir valores, datos incorrectos")
        
        return lista_valores


    
        

    def prepara_sentencia(self, sentencia):
        #quita espacios y coloca las letras en minuscula
        exprecion = (sentencia.replace(" ", "")).lower()
        return exprecion


    def despejar_dividir_dos_incognitas(self, matriz_con_numeros):
        #dividir con x y y para luego remplazar

        matriz = np.zeros((2,2))
     

        matriz[0][0] = matriz_con_numeros[0][2] / matriz_con_numeros[0][0]
        matriz[0][1] = (matriz_con_numeros[0][1]*-1) / matriz_con_numeros[0][0]

        matriz[1][0] = matriz_con_numeros[1][2] / matriz_con_numeros[1][1]
        matriz[1][1] = (matriz_con_numeros[1][0]*-1) / matriz_con_numeros[1][1]




        return matriz



    
    def encontrar_raiz_dos_incognitas(self, x0, y0, matriz, iteraciones):
        #se calculan el valor de x y y
        Di = 100
        x = x0
        y = y0

        valor_error = 0
        xnuevo = 0
        ynuevo = 0

        r = 0
        resultados = []

        while(Di > valor_error and r < iteraciones):
            r+=1
            xnuevo = matriz[0][0] + matriz[0][1]*y
            ynuevo = matriz[1][0] + matriz[1][1]*x

            partex = np.abs(x-xnuevo)
            partey = np.abs(y-ynuevo)

            if(partex > partey):

                Di = partex

            else:

                Di = partey

            x = xnuevo
            y = ynuevo

            resultados.append(["{:.4f}".format(xnuevo),"{:.4f}".format(ynuevo),"{:.4f}".format(Di)])

            #print("x nuevo:",xnuevo, ", y nuevo:", ynuevo, "di:", Di)

        return resultados


    def despejar_dividir_tres_incognitas(self, matriz_con_numeros):
        #dividir con x y y para luego remplazar

        matriz = np.zeros((3,3))
     

        matriz[0][0] = matriz_con_numeros[0][3] / matriz_con_numeros[0][0]
        matriz[0][1] = (matriz_con_numeros[0][1]*-1) / matriz_con_numeros[0][0]
        matriz[0][2] = (matriz_con_numeros[0][2]*-1) / matriz_con_numeros[0][0]

        matriz[1][0] = matriz_con_numeros[1][3] / matriz_con_numeros[1][1]
        matriz[1][1] = (matriz_con_numeros[1][0]*-1) / matriz_con_numeros[1][1]
        matriz[1][2] = (matriz_con_numeros[1][2]*-1) / matriz_con_numeros[1][1]
        

        matriz[2][0] = matriz_con_numeros[2][3] / matriz_con_numeros[2][2]
        matriz[2][1] = (matriz_con_numeros[2][0]*-1) / matriz_con_numeros[2][2]
        matriz[2][2] = (matriz_con_numeros[2][1]*-1) / matriz_con_numeros[2][2]




        return matriz



    
    def encontrar_raiz_tres_incognitas(self,  x0, y0, z0, matriz, iteraciones):
        #se calculan el valor de x y y
       
        Di = 100
        x = x0
        y = y0
        z = z0
        valor_error = 0

        xnuevo = 0
        ynuevo = 0
        znuevo = 0
        r = 0

        resultados = []

        while(Di > valor_error and r < iteraciones):
            r+=1
            xnuevo = matriz[0][0] + matriz[0][1]*y + matriz[0][2]*z
            ynuevo = matriz[1][0] + matriz[1][1]*x + matriz[1][2]*z
            znuevo = matriz[2][0] + matriz[2][1]*x + matriz[2][2]*y

            partex = np.abs(x-xnuevo)
            partey = np.abs(y-ynuevo)
            partez = np.abs(z-znuevo)

            if(partex > partey and partex > partez):

                Di = partex

            elif(partey > partex and partey > partez):

                Di = partey

            else:
                Di = partez

            
            x = xnuevo
            y = ynuevo
            z = znuevo
            resultados.append(["{:.4f}".format(xnuevo),"{:.4f}".format(ynuevo),"{:.4f}".format(znuevo),"{:.4f}".format(Di)])
            #print("x nuevo:",xnuevo, ", y nuevo:", ynuevo, "Z nuevo:", znuevo, "di:", Di)

        return resultados

           


    def proceso_jacobi(self, lista_expresion, valorx, valory, valorz, valor_iteraciones):

        lista_datos_expresion = []
        resultados = []

        for expresion in lista_expresion:

            lista_datos_expresion.append(self.valores_ecuacion_buscar_expreciones_regulares(expresion))

        if(len(lista_datos_expresion) == 2):
            
            matriz = self.despejar_dividir_dos_incognitas(lista_datos_expresion)
            resultados = self.encontrar_raiz_dos_incognitas(valorx,valory,matriz,valor_iteraciones)


        else:

            matriz = self.despejar_dividir_tres_incognitas(lista_datos_expresion)
            resultados = self.encontrar_raiz_tres_incognitas(valorx,valory, valorz,matriz,valor_iteraciones )


        return resultados







if(__name__ == "__main__"):
    obj = Jacobi()
    lista = [[10,0,-1, -1],[4,12,-4,8], [4,4,10,4]]
    matriz = obj.despejar_dividir_tres_incognitas(lista)
    obj.encontrar_raiz_tres_incognitas(1,2,0,matriz,10)








