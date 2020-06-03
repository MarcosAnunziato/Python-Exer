# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:17:32 2020

@author: marco
"""
# desfio 22 aula 09 

nome = str(input('Digite seu nome completo: '))

print(nome.upper())

print(nome.lower())   

print(len(nome))

print(nome.count(' '))

letras = len(nome) - (nome.count(' '))
print(letras)


lista = (nome.split())
primeiro = lista[0]
print(primeiro)
print(len(primeiro))

