# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:41:12 2020

@author: marco
"""
# Desafio 11




largura = float(input('Digite a largura: '))
altura = float(input('Digite o altura: '))
area = largura * altura
pinta_area = area/2
lata_dezoito = 18
compra_lata = pinta_area // lata_dezoito
galao = pinta_area % lata_dezoito
galao_tinta = galao // 3.6
print(f' Será necessario para uma area de {area:.2f} metros {pinta_area:.2f} litros de tinta \n para pintura da parede.')
# Compremento extrafora do enunciado
print('********Lista de compras***********')
lata_dezoito = 18
compra_lata = pinta_area // lata_dezoito
galao = pinta_area % lata_dezoito
galao_tinta = galao // 3.6
print(' Compre \n{:.0f} latas de 18 litros\n e {:.0f} galões de 3.6.'. format(compra_lata, galao_tinta))