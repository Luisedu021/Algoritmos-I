import math

try:
    while True:
        leitura = input()
        n = int(input())
        contador = 0
        ciclos = 0
        while contador < len(leitura):
            if leitura[contador] == 'R':
                qtd_r = 0
                while contador < len(leitura) and leitura[contador] == 'R':
                    qtd_r += 1
                    contador += 1
                ciclos += math.ceil(qtd_r / n)
            elif leitura[contador] == 'W':
                ciclos += 1
                contador += 1
        print(ciclos)

except EOFError:
    pass

