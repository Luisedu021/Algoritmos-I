print('{}Comparador numérico\033[m'.format('\033[3;32m'))
numero1,numero2 = map(float,input('Digite dois números:').split())
if numero1 >   numero2:
    print('O número {} é maior que {}'.format(numero1,numero2))
elif numero1 < numero2:
    print('O número {} é menor que {}'.format(numero1,numero2))
else:
    print('Eles são iguais entre si')
