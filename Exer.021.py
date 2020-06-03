# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:07:41 2020

@author: marco
"""


# Desafio 21

import pygame
# Inicializando o PyGame
pygame.mixer.init()
pygame.init()

# Carregando o arquivo MP3 e executando
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(10)
pygame.event.wait()


