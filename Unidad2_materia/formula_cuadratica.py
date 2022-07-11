# -*- coding: utf-8 -*-
# #!/usr/bin/env python

import sys
import math
repetir = 'si'

while repetir != 'no':
    try:

        if repetir == 'si':

            a = int(input('Valor de a: '))
            b = int(input('Valor de b: '))
            c = int(input('Valor de c: '))

            x1 = 0
            x2 = 0
            i1 = 0
            i2 = 0

            if a == 0:
                if b != 0:
                    x1 = -c / b

                else:
                    print('Solución trivial')
            else:
                disc = (math.pow(b, 2)) - (4 * a * c)

                if disc >= 0:
                    x1 = (-b + math.sqrt(disc)) / (2 * a)
                    x2 = (-b - math.sqrt(disc)) / (2 * a)
                else:
                    x1 = -b / (2 * a)
                    x2 = x1
                    i1 = math.sqrt(abs(disc)) / (2 * a)
                    i2 = -i1
            
            print('r1= ' + str(x1))
            print('r2= ' + str(x2))
            print('i1= ' + str(i1))
            print('i2= ' + str(i2))

            print('¿Desea repetir?:')
            repetir = str(input(''))

            if repetir == 'no':
                sys.exit()
            
            elif repetir == 'si':
                pass
            
            else: 
                print('¿Si o no pues?')
                repetir = str(input(''))
    except ValueError:
        print('Por favor usa valores enteros')