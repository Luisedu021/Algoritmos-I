"""Faça um programa que gere números inteiros aleatórios entre 1 e 10 e calcule a some desses,até seja gerado um número num que foi informado'"""
from random import randint
num = int(input('Informe um número de 1 até 10:'))
contador = 0
sorteador = randint(1,10)
while num != sorteador:
    contador += num
    sorteador = randint(1,10)
    print(sorteador)

print(contador)
print(sorteador)



