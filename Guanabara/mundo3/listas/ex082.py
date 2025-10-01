lista = list()
lista_pares = list()
lista_impares = list()
while True:
    valor  = int(input('Digite um valor: '))
    lista.append(valor)
    verificar = input('Quer continuar?[S/N]')[0]
    if verificar in 'Nn':
        break

for c in range(0,len(lista)):
    if lista[c] % 2 == 0:
        lista_pares.append(lista[c])
    else:
        lista_impares.append(lista[c])

print(f'A lista completa é: {lista}')

print(f'A lista com apenas valores pares é: {lista_pares}')

print(f'A lista com apenas valores impares é: {lista_impares}')
