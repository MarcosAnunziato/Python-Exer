# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:34:15 2020

@author: marco
"""

# Desafio 20

import random
# sample = amostra

names = ['Marcos', 'Meire', 'Luiza', 'Davi']                    
print(random.sample(names, 4))                    

# solução do professor
# shuffle = embaralhar

random.shuffle(names)
print(names)
