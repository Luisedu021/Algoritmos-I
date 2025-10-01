from ex086 import escrever_matriz

matriz = []
for i in range(0,3):
    linha = []
    for j in range(0,3):
        n = int(input(f'Digite um valor para [{i},{j}]: '))
        linha.append(n)
    matriz.append(linha)

escrever_matriz(matriz)

def soma(matriz):
    soma = 0
    for pos,linha in enumerate(matriz):
        for elemento in linha:
            if elemento % 2 == 0:
                soma += elemento
    return soma

def soma_ter_coluna(matriz):
    soma = 0
    for linha in matriz:
        for pos,elemento in enumerate(linha):
            if pos == 2:
                soma += elemento
    return soma

def maior_segunda_linha(matriz):

    for pos,linha in enumerate(matriz):
        for pos1,elemento1 in enumerate(linha):
            if pos == 2:
                if pos1 == 0:
                    elementomaior = elemento1
                else:
                    if elemento1 > elementomaior:
                        elementomaior = elemento1


print(f'A soma da matriz é: {soma(matriz)}')
print(f'A soma da terceira coluna da matriz é: {soma_ter_coluna(matriz)}')
print(f'O maior da segunda linha é: {maior_segunda_linha(matriz)}')

