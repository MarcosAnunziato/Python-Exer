# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 22:33:51 2020

@author: marco
"""


n = input('Digite algo: ')
print('É um número?',n.isnumeric())

print('É alfabético?',n.isalpha ())

print('Está em  maiscula?',n.isupper())

print('é composta por digitos?',n.isdigit ())

print('São decimais?',n.isdecimal())

print('É um identificador?', n.isidentifier())

print('Está em minuscula?', n.islower())

print(n.isprintable())

print('Só tem espaço',n.isspace())

print(n.istitle())
