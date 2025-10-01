#importação do módulo de raiz quadrada só pra facilitar os cálculos
from math import sqrt
#entrada do usuário
a, b, c = map(float,input().split())
#cálculo do delta
delta = (b**2) - (4*a*c)
#condições de existência
if a == 0 or delta <0:
    print('Impossivel calcular')
else:
    x1 = (-b + sqrt(delta))/(2*a)
    x2 = (-b - sqrt(delta))/(2*a)
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')
