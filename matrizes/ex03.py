def conta_vizinhos(matriz, linha, coluna):
    drones = 0
    dx = [-1, 0, 1]
    dy = [-1, 0, 1]

    for i in range(3):  # loop externo sobre dx
        for j in range(3):  # loop interno sobre dy
            if dx[i] == 0 and dy[j] == 0:
                continue  # ignora a posição central (a própria célula)

            vizinho_linha = linha + dx[i]
            vizinho_coluna = coluna + dy[j]

            if (vizinho_linha >= 0 and vizinho_linha < len(matriz) and
                vizinho_coluna >= 0 and vizinho_coluna < len(matriz[0])):
                if matriz[vizinho_linha][vizinho_coluna] == 1:
                    drones = drones + 1

    return drones
matriz = [  [0, 1, 0],
                     [0, 1, 0],
                     [0, 1, 1]
             ]

for pos,linha in enumerate(matriz):

    for pos1,coluna in enumerate(linha):
        print(matriz[pos][pos1],end = ' ')
    print()

print(conta_vizinhos(matriz,0,2))