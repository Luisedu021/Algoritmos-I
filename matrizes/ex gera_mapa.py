from ex03p2 import conta_vizinhos

def gera_mapa(matriz):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    novo_mapa = []

    for i in range(num_linhas):
        linha_nova = []
        for j in range(num_colunas):
            if matriz[i][j] == 1:
                linha_nova.append(9)
            else:
                drones = conta_vizinhos(matriz, i, j)
                linha_nova.append(drones)
        # adiciona linha ao novo mapa
        novo_mapa.append(linha_nova)

    return novo_mapa

# Impressão formatada
def imprime_mapa(mapa):
    num_linhas = len(mapa)
    num_colunas = len(mapa[0])

    for i in range(num_linhas):
        for j in range(num_colunas):
            print(mapa[i][j], end="")
        print()  # nova linha após cada linha da matriz


# Exemplo de uso

# Leitura das dimensões da matriz
n, m = map(int, input().split())

# Leitura das linhas da matriz
matriz = []
for _ in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

# Chamada das funções que gera o mapa e imprime o mapa resultante
novo_mapa = gera_mapa(matriz)
imprime_mapa(novo_mapa)