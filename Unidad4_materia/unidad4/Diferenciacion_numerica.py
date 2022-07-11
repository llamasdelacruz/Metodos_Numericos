

# metodos de diferenciacion numerica de tres y cinco puntos
# como la funcion no nos es dada, solo necesitamos los puntos ya evaluados en dicha funcion
class Tres_Puntos():


    def formula(self,punto1, punto2, punto3, h):
        # aproximar la derivada con el termino siguiente 
        # solo necesitamos los tres primeros puntos y el espacio h


        #aproximacion hacia la derecha
        x1 = (-3*punto1+4*punto2-punto3)/(2*h)

        #aproximacion al centro
        #x2 = ( (punto1-h) + (punto1 + h))/(2*h)

        #aproximacion hacia la izquierda
        #x3 = ( (punto1-(2*h)) - 4*(punto1-h) + 3*punto1)/(2*h)

        #resultados = [x1,x2, x3]

        return x1

   


class Cinco_Puntos():

    def formula(self,punto1, punto2, punto3, punto4, h):

        # aproximar la derivada con el termino siguiente
        # solo me pasas los puntos ya evaluados en la funcion

        resultado = ( (punto1)-8*(punto2)+8*(punto3)-(punto4))/(12*h)

        return resultado





