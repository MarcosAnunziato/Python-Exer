# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:41:34 2020

@author: marco
"""


def vogal(letra):
    vogal = "aeiouAEIOU"
    return letra in vogal

letra = input ("Digite uma letra: ")
print(vogal(letra))
