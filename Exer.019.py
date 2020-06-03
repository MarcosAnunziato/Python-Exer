# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:54:49 2020

@author: marco
"""

# desafio 19

import random

x = random.randint(0,3)
lista = ['Marcos', 'Meire', 'Luiza', 'Davi']
print(lista[x])

# solução do Professor Guanabara

n1 = 1 #str(input('primeiro aluno: '))
n2 = 2 #str(input('Segundo  aluno: '))
n3 = 3 #str(input('Terceiro aluno: '))
n4 = 4 #str(input('Quarto   aluno: '))
n5 = 5
list_a = [n1, n2, n3, n4, n5]
escolhido = random.choice(list_a)
print('O aluno escolhido foi {}'.format(escolhido))
num  = input('Digite um número ')
if num == escolhido:
    print('Acertou!')
else:
    print('Errouuuu....')   
print('Fim')    
print('Voce acertou' if num == escolhido else 'Errouuuu...')