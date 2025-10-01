#entrada de usuário
A, B, C = map(float, input().split())
#ordenando os valores para manipulação e verificação da condição de existência
ord = sorted([A,B,C])
A = ord[2]
B = ord[1]
C = ord[0]
#adicionando a condição de existência
if  A >= B + C :
    print('NAO FORMA TRIANGULO')
#adicionando as condições dos tipos de triangulos
else:
    if A**2 == B**2 + C**2 :
        print('TRIANGULO RETANGULO')
    if A**2 > B**2 + C**2 :
        print('TRIANGULO OBTUSANGULO')
    if A**2 < B**2 + C**2:
        print('TRIANGULO ACUTANGULO')
    if  A == B ==C:
        print('TRIANGULO EQUILATERO')
    elif  A == B != C or A == C != B or B == C != A :
        print('TRIANGULO ISOSCeLES'.capitalize())






