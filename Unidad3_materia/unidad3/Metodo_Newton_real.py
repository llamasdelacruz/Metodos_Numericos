import numpy as np
import sympy as sp

class Newton():

    def F(self,X_Y):

        x = X_Y[0]
        y = X_Y[1]

        f1 = eval(str(self.f1))
        f2 = eval(str(self.f2))

        return np.array([float(f1),float(f2)])

    def DF(self,X_Y):

        x_simbolo,y_simbolo = sp.symbols('x y')#colocamos los simbolos

        #derivamos las expresiones
        f1_derivadax = sp.diff(self.f1,x_simbolo)
        f1_derivaday = sp.diff(self.f1,y_simbolo)

        f2_derivadax = sp.diff(self.f2, x_simbolo)
        f2_derivaday = sp.diff(self.f2,y_simbolo)

        #establecemos los valores x y y para que al evaluar nos 
        x = X_Y[0]
        y = X_Y[1]

        #evaluamos con la expresion que nos entrega simpy convertida a str
        f1_evaluacionx = eval(str(f1_derivadax))
        f1_evaluaciony = eval(str(f1_derivaday))

        f2_evaluacionx = eval(str(f2_derivadax))
        f2_evaluaciony = eval(str(f2_derivaday))



        return np.array([ [f1_evaluacionx,f1_evaluaciony], [f2_evaluacionx, f2_evaluaciony] ] )

    def proceso(self, expresion1, expresion2, xentrada, yentrada, iteraciones):
        #se hacen colocan las expresiones y se crea el array con las dos soluciones iniciales

        N = iteraciones
        X_Y = np.array([xentrada,yentrada])
        self.f1 = expresion1
        self.f2 = expresion2
        resultados = []

        for k in range(N):

            xold = X_Y
            Jinv = np.linalg.inv(self.DF(X_Y))
            X_Y = X_Y-np.dot(Jinv,self.F(X_Y))
            e = np.linalg.norm(X_Y-xold)

            #print(k, X_Y, e)
            resultados.append([X_Y,e])

            if(e<1e-10):
                break

        return resultados

if(__name__ == "__main__"):
    m = Newton()
    m.proceso("x**2+y**2-1","(4/9)*x**2+4*y**2-1", -1,1)