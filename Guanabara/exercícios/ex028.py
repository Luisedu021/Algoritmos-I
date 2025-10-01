import random
from time import sleep
n=random.randint(0,5) #faz o computador pensar em um número aleatório
#fazendo o usuário adivinhar o numero
nu=int(input('Digite um número entre 0 e 5:'))
print('PROCESSANDO...')
sleep(2)
if nu==n:
    print('Parabéns,você acertou!O número era{}!'.format(n))
else:
    print('Voce errou,o número era {}!'.format(n))
