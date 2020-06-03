# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:10:42 2020

@author: marco
"""

# Desafio 17

import math
# ou from math import hypot

a = float(input('Digite o valor do cateto adjacente do trinagulo: '))
b = float(input('digite o valor do cateto oposto do triangulo: '))

print(' O valor da HIPOTENUSA  é {:.2f}'.format(math.hypot(a,b)))