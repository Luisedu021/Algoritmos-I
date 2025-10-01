def main():
    import sys

    linhas = [input().strip() for _ in range(4)]
    colunas = len(linhas[0])
    matriz = [[int(linhas[l][c]) for c in range(colunas)] for l in range(4)]

    numeros = []
    for c in range(colunas):
        num = 0
        for l in range(4):
            num = num * 10 + matriz[l][c]
        numeros.append(num)

    F = numeros[0]
    L = numeros[-1]
    mensagem = ''
    for Mi in numeros[1:-1]:
        Ci = (F * Mi + L) % 257
        mensagem += chr(Ci)
    print(mensagem)

if __name__ == "__main__":
    main()