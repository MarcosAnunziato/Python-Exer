# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:17:29 2020

@author: marco
"""

# Desafio 001
import emoji
nome = input('Digite o seu nome ')
Boas_Vindas = ('Olá,')
print(Boas_Vindas,  nome)
print(emoji.emojize(f'Olá, {nome} :earth_americas:', use_aliases=True))