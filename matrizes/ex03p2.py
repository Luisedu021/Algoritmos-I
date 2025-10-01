matriz = [
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
]



def conta_vizinhos(matriz, linha, coluna):
    cont = 0
    if matriz[linha][coluna] == 0:
        if coluna == 0:
            if linha != 0:
                if matriz[linha - 1][coluna] == 1:
                    cont += 1
                if matriz[linha][coluna] == 1:
                    cont += 1
                if matriz[linha][coluna + 1] == 1:
                    cont += 1
            else:
                if matriz[linha + 1][coluna] == 1:
                    cont += 1
                if matriz[linha][coluna + 1] == 1:
                    cont += 1

        elif coluna == 1 or coluna == 2:
            if linha != 0 and linha != 3:
                if matriz[linha - 1][coluna] == 1:
                    cont += 1
                if matriz[linha ][coluna - 1] == 1:
                    cont += 1
                if matriz[linha + 1][coluna ] == 1:
                    cont += 1
                if matriz[linha ][coluna + 1] == 1:
                    cont += 1
            else:
                if linha == 0  :
                     if matriz[linha][coluna - 1] == 1:
                        cont += 1

                     if matriz[linha + 1][coluna] == 1:
                         cont += 1

        elif linha == 3:
                if matriz[linha - 1][coluna] == 1:
                    cont += 1
                if matriz[linha][coluna - 1] == 1:
                    cont += 1
        else:
                if matriz[linha][coluna - 1] == 1:
                    cont += 1
                if matriz[linha - 1][coluna] == 1:
                    cont += 1
                if matriz[linha + 1][coluna] == 1:
                    cont += 1


    return cont



