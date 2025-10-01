nomes = list()
pesos = list()
cont = 0
while True:
    nome = input('Informe seu nome: ')
    nomes.append(nome)
    peso = float(input('Informe seu peso:  '))
    pesos.append(peso)
    cont += 1
    verif = input('Quer continuar? [S/N]')
    if verif in 'Nn':
        break

maximo = max(pesos)
minimo = min(pesos)


print(f'Ao todo,você cadastrou {cont} pessoas')
print(f'O maior peso foi de {maximo:.2f} Kg.Peso de, ',end = ' ')
for pos,peso in enumerate(pesos):
    if peso == maximo:
        print(nomes[pos], end =  ' ')
print(f'O menor peso foi de {minimo:.2f} Kg.Peso de ',end = ' ')
for pos,peso in enumerate(pesos):
    if peso == minimo:
        print(nomes[pos], end=' ')
