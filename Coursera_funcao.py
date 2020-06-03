# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:03:19 2020

@author: marco
"""


def maximo(x, y):
    if (x > y):
        return x
    else:
        return y

x = input("digite um número inteiro: ")
x = int(x)
y = input("digite um número inteiro: ") 
y = int(y)   
 
maximo(x,y)