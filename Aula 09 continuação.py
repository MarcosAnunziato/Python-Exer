# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 22:14:01 2020

@author: marco
"""
frase = 'Curso em Video Python'

print('''jçlkdjfçlkjafjaçdlkfjalkdsjfkladsjfçlkj
kljdfçkjaçkfjçakdjfçklajdfçklj
çklafçlkjasçdfjçakljfçlkajdfçlkjadçflkjçaskljf''')

# ************  cambinação    **************

print(frase.upper().count('P')) # Conta quantos P maiusculo em na frase()

print(len(frase.strip()))

dividido = frase.split()
print(dividido[0:2])

print(dividido[2:])

print(dividido[2][3]) # m 'Curso em Vid(e)o Python'ostra 

