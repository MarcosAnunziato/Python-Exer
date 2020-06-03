>import math
import sys
a = int(input('Digite um n´mero para valor de "a" '))
b = int(input('Digite um n´mero para valor de "b" '))
c = int(input('Digite um n´mero para valor de "c" '))
d =((b^2)-4*a*c)

if d < 0:
    print('help')
else:
    m1 = math.sqrt(d)
    x1=(-b+m1)/(2*a)
    x2=(-b-m1)/(2*a)
    print ("Raiz aproximada de X1= %s.") % x1
    print ("Raiz aproximada de X2= %s.") % x2
