# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:57:23 2020

@author: marco
"""


def maior_primo():
  for x in range(1,200):
      cont = 0
  for y in range(1,x+1):
    if x%y==0:
      cont+=1
  if cont <=2:
      primos.append(x)
      maior_numero = max(maior_primo)
      return maior_numero
 print(maior_numero) 