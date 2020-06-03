# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:29:45 2020

@author: marco
"""



preco = float(input('Digite o preço do produto: '))

preco_desconto = preco - ((preco * 5)/100)
print(f'O preço original é de R$ {preco:.2f} com 5% de descontos fica F$ {preco_desconto:.2f}.')