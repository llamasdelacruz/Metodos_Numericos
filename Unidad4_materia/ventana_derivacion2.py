import re
import sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication
from PyQt5 import uic
from PyQt5 import QtWidgets
import ctypes #getSystemMetr

#imports codigo propio
#se debe poner toda la ruta desde el paqute raiz para que python lo capte
from Unidad4_materia.unidad4.Diferenciacion_numerica import Tres_Puntos, Cinco_Puntos

class Ventana_derivacion2(QDialog):

    def __init__(self, ventana_principal):

        self.ventana_principal = ventana_principal

        QDialog.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("Unidad4_materia/derivacion_2.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)

        # variables 
        self.tres_puntos = Tres_Puntos()
        self.cinco_puntos = Cinco_Puntos()

        # colocar los metodos en los botones
        self.tres_puntos_boton.clicked.connect(self.proceso_tres_puntos)
        self.cinco_puntos_boton.clicked.connect(self.proceso_cinco_puntos)

    def proceso_tres_puntos(self):
        
        if(self.puntos != "" and self.valorH != ""):

            #lista de puntos dados por el usuario, se extraen con expresiones regulares, esta expresion permite numero positvos y negativos con decimales
            puntos = [float(s) for s in re.findall(r'[+-]?\d+(?:\.\d+)?', self.puntos.text())]
            print(puntos)
            if(len(puntos) == 3):
                valor_h = float(self.valorH.text())
                resultado = self.tres_puntos.formula(punto1=puntos[0], punto2=puntos[1], punto3=puntos[2], h=valor_h)
                self.ver_resultados.setText(str(resultado))
                self.ver_resultados.adjustSize()

            else:

                QMessageBox.warning(self, "hey !!", "Debes colocar tres puntos para usar este metodo", QMessageBox.Discard)

        else:
            QMessageBox.warning(self, "hey !!", "Debes rellenar todos los campos", QMessageBox.Discard)

    def proceso_cinco_puntos(self):
        # realiza el proceso de cico puntos solo verificando que se tengan valores
        if(self.puntos != "" and self.valorH != ""):

            #lista de puntos dados por el usuario, se extraen con expresiones regulares
            puntos = [float(s) for s in re.findall(r'[+-]?\d+(?:\.\d+)?', self.puntos.text())]
            
            if(len(puntos) == 4):

                valor_h = float(self.valorH.text())
                resultado = self.cinco_puntos.formula(punto1=puntos[0], punto2=puntos[1], punto3=puntos[2], punto4=puntos[3],h=valor_h)
                self.ver_resultados.setText(str(resultado))
                self.ver_resultados.adjustSize()

            else:

                QMessageBox.warning(self, "hey !!", "Debes colocar cuatro puntos para usar este metodo", QMessageBox.Discard)

        else:
           
           QMessageBox.warning(self, "hey !!", "Debes rellenar todos los campos", QMessageBox.Discard)

    def closeEvent(self, event):

        self.ventana_principal.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    dialogo = Ventana_derivacion2()
    dialogo.show()
    app.exec_()