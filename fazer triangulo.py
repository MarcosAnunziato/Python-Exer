# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:20:10 2020

@author: marco
"""


ab = int(input('Digite um número inteiro: '))
cd = int(input('Digite um número inteiro: '))
ef = int(input('Digite um número inteiro: '))
if ab + cd >= ef and ab + ef >= cd and ef + cd >= ab:
    print('É possivel fazer um triangulo.')
else:
    print('Não é possivel fazer um triangulo.')    
    