print('Insira os dados abaixo:')
ca=float(input('Digite o valor do cateto adjacente:'))
hi=float(input('Digite o valor do cateto hipotenusa:'))
F=float(input('Digite o valor da força aplicada sobre o objeto em N:'))
d=float(input('Digite o valor da distância percorrida:'))
cos=ca/hi
T=F*d*cos
print('O valor do trabalho realizado pelo corpo é de {} joules'.format(T))
