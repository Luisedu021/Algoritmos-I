import random
n1 = random.randint(0, 10000)
n2 = random.randint(0, 10000)
n3 = random.randint(0, 10000)
n4 = random.randint(0, 10000)
n5 = random.randint(0, 10000)
numeros = (n1, n2, n3, n4, n5)
#fazendo na raça
for i in range(0,len(numeros)):
    if i == 0:
        maior = numeros[0]
    else:
        if numeros[i] > maior:
            maior = numeros[i]

for i in range(0,len(numeros)):
    if i == 0:
        menor = numeros[0]
    else:
        if numeros[i] < menor:
            menor = numeros[i]

print(menor)
print(maior)

#fazendo na boa vida do python
maximo = max(numeros)
minimo = min(numeros)
print(f'Os valores sorteados foram: {n1},  {n2}, {n3}, {n4} e {n5}')
print(f'O maior valor sorteado foi {maximo}')
print(f'O menor valor sorteado foi {minimo}')
