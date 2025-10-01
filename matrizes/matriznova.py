l,c = map(int,input().split())
matriz = []
for i in range(l):
    linha_nova = []

    for j in range(c):
        linha_nova.append(int(input()))
    matriz.append(linha_nova)




for linha in matriz:
    for coluna in linha:
        print(coluna,end = ' ')
    print()
