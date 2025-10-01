from random import randint

contador = 0

sorteado = randint(0,10)
print(sorteado)
ver = 20
while ver != sorteado:
    ver = int(input('Digite um número:'))
    contador += 1
    if (ver)  == sorteado:
        print('Parabéns,acertou!!')

print('Ao final você digitou {} números até acertar'.format(contador))

