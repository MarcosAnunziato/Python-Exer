# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:30:26 2020

@author: marco
"""

# Desafio 18

import math
ang=int(input('Digite um ângulo qualquer: '))
rad=math.radians(ang)
#print('O valor desse ângulo em radianos é: {} '.format(rad))
cos=math.cos(rad)
sen=math.sin(rad)
tan=math.tan(rad)

print('O cosseno desse ângulo é: {:.2f}\n'
      'O seno desse ângulo é: {:.2f} \n'
      'A tangente desse ângulo é: {:.2f}'.format(cos,sen,tan))
