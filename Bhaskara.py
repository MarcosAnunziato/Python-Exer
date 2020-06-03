import math
a = int(input('Digite um valor para a: '))
b = int(input('Digite um valor para b: '))
c = int(input('Digite um valor para c: '))
x = 0
x_a = 0
delta = (b**2) -4*(a*c)
print(delta)
if delta < 0:
   print("esta equação não possui raízes reais")
if delta > 0:
   raiz_delta = math.sqrt(delta)
   x_a = (-b + raiz_delta) / (2*a)
   x_b = (-b - raiz_delta) / (2*a)
   if delta == 0:
    x_a = 0 and  x_b > 0  
    x = x_b
else:
    x_b = 0 and  x_a > 0
    x = x_a
    print("as raízes da equação é", x)
if x_a != 0 or x_b != 0:
   x_a < x_b 
   menor = x_a
   maior = x_b
else:
   x_b < x_a
   menor = x_b
   maior = x_a
   print("as raízes da equação são", menor, "e", maior,)

