lista = []
posicoesmax = []
posicoesmin = []
max = ''
for i in range(0,5):
    lista.append(int(input(f'Digite um valor na posição {i} : ')))
    if i ==0:
        max = min = list[i]

    elif lista[i] > max:
        max = lista[i]
    elif lista[i] < min:
        min = lista[i]

for pos,item in enumerate(lista):
    if item == max:
        posicoesmax.append(pos)
    if item == min:
        posicoesmin.append(pos)

print(f'O maior valor digitado foi {max} nas posições ',end = ' ')
for item in range(len(posicoesmax)):
    if item == (len(posicoesmax )- 1):
        print(f'{posicoesmax[item]}...')
    else:
        print(f'{posicoesmax[item]}...', end = ' ')


print(f'O menor valor digitado foi {min} nas posições',end = ' ')
for item in posicoesmin:
    print(f'{item} ... ',end = ' ')
