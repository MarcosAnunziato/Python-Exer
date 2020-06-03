# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 10:57:51 2020

@author: marco
"""


nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))
print('Alinha a DIREITA {:>20}!'.format(nome))
print('Alinha a ESQUERDA {:<20}!'.format(nome))
print('Alinha a CENTRO {:^20}!'.format(nome))
print('Alinha a DIREITA {:=^20}!'.format(nome))
