4
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 11:21:27 2020

@author: marco
"""


n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira {} e potência {}'.format(di, e))

# Não quebrar a linha end='' 
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d),end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))
# Quebra linha \n
print('A soma é {}, \n o produto é {} \n e a divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira {}\n e potência {}'.format(di, e))
