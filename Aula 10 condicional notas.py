# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:53:26 2020

@author: marco
"""


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(n))
if n >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruin! ESTUDE MAIS!')    