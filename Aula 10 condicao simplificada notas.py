# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 21:06:42 2020

@author: marco
"""


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(n))
print('PARABÉNS!' if n >= 6 else 'ESTUDE MAIS!')