lista = [[],[]]
lista_pares = lista[0]


for i in range(0,7):
    n =int(input(f'Digite o {i+1}o. valor: '))
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista[1].append(n)


def bubble_sort(lista):
    tam = len(lista)
    for j in range(tam - 1):
        for i in range(tam-1):
            if lista[i]  > lista[i+1]:
                lista[i], lista[i + 1] = lista [i + 1] , lista[i]
    return lista

print(f'Os valores pares digitados foram: {bubble_sort(lista_pares)}')
print(f'Os valores impares digitados foram: {bubble_sort(lista[1])}')