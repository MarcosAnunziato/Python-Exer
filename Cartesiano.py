import math
xb = int(input('Digite um xb: '))
xa = int(input('Digite um xa: '))
yb = int(input('Digite um yb: '))
ya = int(input('Digite um ya: '))
dab =  math.sqrt((xb-xa)**2)+((yb-ya)**2)
print(dab)
if dab == 10 or dab > 10:
    print('longe')
else:   
    print('perto')    
