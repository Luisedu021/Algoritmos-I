alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
nt = int(input())
for i in range(nt):
    linhas = int(input())
    matriz = []
    for i in range(linhas):
        elemento = input()
        colunas = len(elemento)
        coluna = []
        for  j in range(colunas):
            coluna.append(elemento[j])
        matriz.append(coluna)


    soma = 0
    for j in range(len(matriz)):
        for i in range(len(coluna)):


            soma += i + j  + alfabeto.index(matriz[j][i])
    print(soma)






'''matriz = []
for i in range(3):
    linha = []
    for j in range(linhas):
        linha.append(alfabeto[j])
    matriz.append(linha)
    
print(matriz)'''
