# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:44:19 2020

@author: marco
"""


nome = str(input('Qual é o seu nome? '))
if nome == 'Marcos':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'. format(nome))    

# Segunda estrutura

nome = str(input('Qual é o seu nome? '))
if nome == 'Marcos':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é diferente')        
print('Bom dia, {}!'. format(nome))   
    