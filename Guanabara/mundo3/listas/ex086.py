'''matriz = []
for i in range(0,3):
    linha = []
    for j in range(0,3):
        n = int(input(f'Digite um valor para [{i},{j}]: '))
        linha.append(n)
    matriz.append(linha)
print()
print('MATRIZ:')'''


def escrever_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f'[ {elemento} ]', end = ' ')
        print()


def determinante(matriz):
    det = ((matriz[0][0]*matriz[1][1]*matriz[2][2]  + matriz[0][1]*matriz[1][2]*matriz[2][0] + matriz[0][2]*matriz[1][0]*matriz[2][1]) -
           (matriz[0][1]*matriz[1][0]*matriz[2][2]  + matriz[2][1]*matriz[1][2]*matriz[0][0] + matriz[2][0]*matriz[1][1]*matriz[0][2]))
    return det
