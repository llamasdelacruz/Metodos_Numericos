
#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from Unidad2_materia.metodos_intervalo.metodo_biseccion import Biseccion_metodo


class Interpolacion(Biseccion_metodo):

    def __init__(self, multiplican, numero_funcion):

        self.multiplican = multiplican
        self.numero_ecuacion = numero_funcion

    
    def encontrar_raiz(self, rango_menor, rango_mayor, toleranciaError):

        resultado = 2
        xr = 0
        xr_anterior =0

        tolerancia = 100
        
        
        i = 0

        while(resultado != 0 and tolerancia > toleranciaError):

      
            xr = rango_mayor - ((self.practica_funcion(rango_mayor)*(rango_menor-rango_mayor))/(self.practica_funcion(rango_menor)-self.practica_funcion(rango_mayor))) 
            
            
            

            resultado = self.practica_funcion(rango_menor) * self.practica_funcion(xr) 
            
            tolerancia = np.abs((xr-xr_anterior)/xr)*100

            if(resultado < 0):

                rango_mayor = xr

            elif(resultado > 0):

                rango_menor = xr

            elif(resultado == 0):
                break

            i+=1

            xr_anterior = xr

            #print(rango_menor, rango_mayor)
        #print(tolerancia)
        return xr
       

        



