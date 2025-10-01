n = int(input())

for j in range(n):
    ninicio, nfim  = map(int, input().split())

    for k in range(ninicio, nfim + 1):
        print(k, end = '')
    contador = nfim - ninicio
    while contador >= 0:
        if contador  > 0:
            print(str(nfim)[:: -1],end = '')
        else:
            print(str(nfim)[:: -1])
        nfim -= 1
        contador -= 1



