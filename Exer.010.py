# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:24:19 2020

@author: marco
"""
# Desafio 10

x = float(input('Quando dinheiro voce tem: '))
dollar = 3.27
conversao = x / dollar
print('Todos os seus R$ {:.2f} Reais valem US$ {:.2f} '.format(x, conversao))