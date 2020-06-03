# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:44:16 2020

@author: marco
"""

# Desafio 16

import math
n = float(input('Digite um número: '))

print('Voce Digitou {} o seu inteiro é {:.0f}'.format(n,n)) ## Essa solução está erra retorna - 0 (menos zero)
#Segunda solução 
#   from math import trunc ===> usando apenas a parte de uma biblioteca
print('Voce digitou {} o seu inteiro é {}'.format(n, math.trunc(n)))
#terceira solução
print('Voce digitou {} o seu inteiro é {}'.format(n, int(n)))