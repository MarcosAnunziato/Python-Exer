# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:28:44 2020

@author: marco
"""



primos=[]
y = int(input('Digite um número: '))
for x in range(1,y):
  cont = 0
  for y in range(1,x+1):
    if x%y==0:
      cont+=1
  if cont <=2:
      primos.append(x)
#print(primos) 
maior_numero = max(primos) 
print(maior_numero)