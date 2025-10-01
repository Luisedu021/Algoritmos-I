def conta_vizinhos(matriz, linha, coluna):
    drones = 0
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])

    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # somente vizinhos ortogonais

    for k in range(4):
        dx = direcoes[k][0]
        dy = direcoes[k][1]

        vizinho_linha = linha + dx
        vizinho_coluna = coluna + dy

        if (vizinho_linha >= 0 and vizinho_linha < num_linhas and
            vizinho_coluna >= 0 and vizinho_coluna < num_colunas):
            if matriz[vizinho_linha][vizinho_coluna] == 1:
                drones = drones + 1
    return drones

#ex de correção