""" Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles."""
from time import sleep
for c in range(10, -1, -1):
    if c < 4:
        print('{}{}\033[m'.format('\033[1;31m', c))
        sleep(1)
    else:
        print(c)
        sleep(1)
print('{}Feliz ano novo!!\033[m'.format('\033[1;34m'))
