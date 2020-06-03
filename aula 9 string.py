# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:37:46 2020

@author: marco
"""


frase = 'Curso em Video Python'

# ======Fatiamento=======

print(frase[9]) # devolve o valor da nona posição resultado 'V'

print(frase[9:13]) #resultado 'Vide'
 
print(frase[9:21]) # Resuldado 'Video Python'

print(frase[:5])  # Resultado 'Curso'

print(frase[9:21:2])# Resultado 'VdoPto'

print(frase[:15]) # Resultado 'Curso em Video '

print(frase[9::3]) # Resultado 'VePh'


#==========Análise de string =========

print(len(frase)) # Resultado conta número de caracteres

print(frase.count('o')) # conta a quantidade do tipo de caracteres

print(frase.count('o', 0 , 13))

print(frase.find('deo')) # em que posição começou a sequencia de caractere 'deo' find = encontrar

print(frase.find('Android')) # retorna posição memos 1 (-1)

print('curso' in frase) # retorna False distigue maiuscula de minuscula
print('Curso' in frase) # retorna True

#********* Transformação****************

print(frase.replace('Python','Android')) # substitui a palavra Python por Android na 

print(frase.upper()) # Maiusculas

print(frase.lower())# minuscula

print(frase.capitalize()) # só a primeira letra da texto fica 

print(frase.title())  # só a primeira palavra da texto fica 

frase = '   Aprenda Python   '

print(frase.strip()) # remove espaços inúteis início e final da frase

print(frase.rstrip()) # remove espaços no final da frase

print(frase.lstrip()) # remove espaço  o início da frase

#********* Divisão ****************

print(frase.split())# transforma em uma lista ['Aprenda', 'Python']

#********Junção***********

print('-'.join(frase)) # Intervalo  - -A-p-r-e-n-d-a- -P-y-t-h-o-n- - - 
















