#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import pandas as pd

import numpy as np

class Reduccion_Metodo():




    def valores_ecuacion_buscar(self, restriccion_sentencia):
        #toma la cadena y separa los valores de x,y, resultado
        
        self.exprecion =  self.prepara_sentencia(restriccion_sentencia)
        self.bandera = False
        try:
            if(self.exprecion.find('x') != -1  and  self.exprecion.find('y') != -1):

                self.x_lineal = pd.eval(self.exprecion[:self.exprecion.find('x')])
                self.y_lineal =  pd.eval(self.exprecion[self.exprecion.find('x')+1: self.exprecion.find('y')])
                self.resultado_lineal = pd.eval(self.exprecion[self.exprecion.find('=')+1:])

                

               
                
               
        except:
            print("Error al introducir valores, datos incorrectos")
        
        return [self.x_lineal, self.y_lineal, self.resultado_lineal]
        

    def prepara_sentencia(self, sentencia):
        #quita espacios y coloca las letras en minuscula
        exprecion = (sentencia.replace(" ", "")).lower()
        return exprecion

    def obtener_puntos(self, valores_variables):
        #obtiene los puntos en base a las restricciones dadas, resolviendo cada par posible por el metodo de reduccion, reduciendo la x
        self.aux = valores_variables
        self.cont = 1
        self.resultado_de_x = 0
        self.resultado_de_y = 0

        for i in valores_variables:
            
            
            for j in range(self.cont, len(valores_variables)):

                #cuando solo esta el valor x o y en el primer for
                if(i[0] == 0 and i[1] != 0 and self.aux[j][0] != 0 and self.aux[j][1] != 0):

                    self.resultado_de_y = i[2]/i[1]
                    self.remplazo_de_y =  self.aux[j][2] - (self.aux[j][1] * self.resultado_de_y)
                    self.resultado_de_x = self.remplazo_de_y / self.aux[j][0]
                    

                elif(i[1] == 0 and i[0] != 0 and self.aux[j][0] != 0 and self.aux[j][1] != 0):

                    self.resultado_de_x = i[2]/i[0]
                    self.remplazo_de_x =  self.aux[j][2] - (self.aux[j][0] * self.resultado_de_x)
                    self.resultado_de_y = self.remplazo_de_x / self.aux[j][1]

                elif(i[0] == 0 and i[1] != 0 and self.aux[j][0] != 0 and self.aux[j][1] == 0):
                    self.resultado_de_x = self.aux[j][2]/self.aux[j][0]
                    self.resultado_de_y = i[2]/i[1]
                
                elif(i[0] != 0 and i[1] == 0 and self.aux[j][0] == 0 and self.aux[j][1] != 0):

                    self.resultado_de_x = i[2]/i[0]
                    self.resultado_de_y = self.aux[j][2]/self.aux[j][1]

                #cuando solo esta el valor x o y en el segundo for
                elif(i[0] != 0 and i[1] != 0 and self.aux[j][0] == 0 and self.aux[j][1] != 0):

                    self.resultado_de_y = self.aux[j][2]/self.aux[j][1]
                    self.remplazo_de_y =  i[2] - (i[1] * self.resultado_de_y)
                    self.resultado_de_x = self.remplazo_de_y / i[0]
                    

                elif(i[1] != 0 and i[0] != 0 and self.aux[j][0] != 0 and self.aux[j][1] == 0):

                    self.resultado_de_x = self.aux[j][2]/self.aux[j][0]
                    self.remplazo_de_x =  i[2] - (i[0] * self.resultado_de_x)
                    self.resultado_de_y = self.remplazo_de_x / i[1]

                elif(i[0] != 0 and i[1] == 0 and self.aux[j][0] == 0 and self.aux[j][1] != 0):
                    self.resultado_de_x = i[2]/i[0]
                    self.resultado_de_y = self.aux[j][2]/self.aux[j][1]
                
                elif(i[0] == 0 and i[1] != 0 and self.aux[j][0] != 0 and self.aux[j][1] == 0):

                    self.resultado_de_x = self.aux[j][2]/self.aux[j][0]
                    self.resultado_de_y = i[2]/i[1]
                else:
                    #print(i, self.aux[j])
                    self.ecuacion1 = i[0] * np.array(self.aux[j])
                    self.ecuacion2 =  -1 * np.array(self.aux[j][0]) * np.array(i)

                    #print(self.ecuacion1, self.ecuacion2)    

                    self.ecuacion_suma = np.add(self.ecuacion1,self.ecuacion2)
                    #print(self.ecuacion_suma, "\n")

                    self.resultado_de_y = self.ecuacion_suma[2]/self.ecuacion_suma[1]

                    self.vector_remplazo = [1,self.resultado_de_y, 1]
                    self.ecuacion_remplazo_sin_dividir = np.multiply(self.ecuacion1, self.vector_remplazo)
                    self.ecuacion_remplazo_restar = self.ecuacion_remplazo_sin_dividir[2]- self.ecuacion_remplazo_sin_dividir[1]
                    self.resultado_de_x = self.ecuacion_remplazo_restar/ self.ecuacion_remplazo_sin_dividir[0]



                

                #self.puntos.append([self.resultado_de_x, self.resultado_de_y]) 

                
                
            self.cont +=1

        return self.resultado_de_x, self.resultado_de_y


if(__name__ == "__main__"):

    obj = Reduccion_Metodo()
    lista = []
    sentencia = input("Dame la ecuacion 1:")
    sentenci2 = input("Dame la ecuacion 2:")
    lista.append(obj.valores_ecuacion_buscar(sentencia))
    lista.append(obj.valores_ecuacion_buscar(sentenci2))
    print(obj.obtener_puntos(lista))