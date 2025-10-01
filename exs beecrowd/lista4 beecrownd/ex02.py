nt = int(input())
for j in range(1,nt + 1):

    n,salto = map(int,input().split())
    lista = []
    index = 0

    for i in range(1,n + 1):
        lista.append(i)

    while len(lista) > 1:

        index = (index + salto - 1 ) % len(lista)

        lista.pop(index)

    print(f'Case {j}: {lista[0]}')

