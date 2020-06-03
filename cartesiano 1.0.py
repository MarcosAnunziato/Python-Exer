import math
xb = int(input('Digite um xb: '))
xa = int(input('Digite um xa: '))
yb = int(input('Digite um yb: '))
ya = int(input('Digite um ya: '))
a = ((xb-xa)**2)
b = ((yb-ya)**2)
dab = math.sqrt(a + b)
print(dab)
if dab == 10 or dab > 10:
    print('longe')
else:   
    print('perto')  
