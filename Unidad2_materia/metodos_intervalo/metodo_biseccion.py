import numpy as np
from sympy import numer, resultant, true




class Biseccion_metodo():

    def __init__(self, multiplican, numero_funcion):

        self.multiplican = multiplican
        self.numero_ecuacion = numero_funcion


        


    def practica_funcion(self, x):

        if(self.numero_ecuacion == 1):

            return (pow(x,self.multiplican[1])*self.multiplican[0]) + (pow(x,self.multiplican[3])*self.multiplican[2]) + self.multiplican[4]

        elif(self.numero_ecuacion == 2):

            return np.exp(self.multiplican[0]*x) + (pow(x,self.multiplican[2])* self.multiplican[1]) + self.multiplican[3]

        elif(self.numero_ecuacion == 3):

            return (pow(x,self.multiplican[1])*self.multiplican[0]) + (pow(x,self.multiplican[3])*self.multiplican[2]) + (self.multiplican[4]*x) + self.multiplican[5]

        elif(self.numero_ecuacion == 4):

            return   (self.multiplican[0]*x)  + np.exp(self.multiplican[1]*x) - np.cos(x)

        elif(self.numero_ecuacion == 5):

            return (np.exp(self.multiplican[1]*x)* self.multiplican[0]) - np.sin(x) + x

    def gx(self, x):

        if(self.numero_ecuacion == 1):

            return ( -1*((pow(x,self.multiplican[3])*self.multiplican[2]) + self.multiplican[4]) /self.multiplican[0]  )** (1/self.multiplican[1])

        elif(self.numero_ecuacion == 2):

            return   ((-1*(self.multiplican[3] + np.exp(self.multiplican[0]*x)))/  self.multiplican[1])**(1/self.multiplican[2])

        elif(self.numero_ecuacion == 3):
        

            return (((pow(x,self.multiplican[1])*self.multiplican[0]) + (pow(x,self.multiplican[3])*self.multiplican[2])  + self.multiplican[5])*-1)/self.multiplican[4]

        elif(self.numero_ecuacion == 4):

            return  -1*(np.exp(self.multiplican[1]*x) - np.cos(x))/self.multiplican[0]

        elif(self.numero_ecuacion == 5):

            return ((np.exp(self.multiplican[1]*x)* self.multiplican[0]) - np.sin(x))*-1



    
    def encontrar_raiz(self, Xl, Xu, rango_error):

        resultado = 2
        xr = 0
        xr_anterior =0

        error = 100
        
        
        i = 0

        multiplicacion = self.practica_funcion(Xl) * self.practica_funcion(Xu)
        

        if( multiplicacion < 0 ):

            while(resultado != 0 and error > rango_error):

                #print("Iteraciion "+ str(i+1))
                #print("Anterior xl = {}, Xu = {}".format(Xl,Xu))

                xr = (Xl + Xu)/2

                #print("xr ="+str(xr))

                resultado = self.practica_funcion(Xl) * self.practica_funcion(xr) 
                #print(str(self.practica_funcion(Xl)) + "  "  +  str(self.practica_funcion(xr)))
                #print("Multiplicacion resultado="+str(resultado))
                

                error = np.abs((xr-xr_anterior)/xr)*100

                
                

                

                if(resultado < 0):

                    Xu = xr
                    #print("xu ="+ str(xr))

                elif(resultado > 0):

                    Xl = xr
                    #print("xl ="+ str(xr))

                elif(resultado == 0):

                    break

                #print(error)
                #print("-----------------------------------------------------------------------\n")

                i+=1
               
                xr_anterior = xr

        else:
            print("no se pudo")

            #print(rango_menor, rango_mayor)
        #print(tolerancia)
        return xr
       

        



if(__name__ == "__main__"):

    obj = Biseccion_metodo(20,1)
    xl = -2
    xu = 0
    print(obj.encontrar_raiz(xl,xu, 0.01))







