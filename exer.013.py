# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:09:45 2020

@author: marco
"""


# Desafio 13

salario = float(input('Digite o salário do funcionário:'))
aumento = salario + (salario * 15)/100
print('O salario atual é de R$ {:.2f} com 15% \n de aumento passa a ser de R$ {:.2f}'.format(salario,salario + (salario * 15)/100))