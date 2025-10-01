try:
    while True:
        lista =[]

        n = int(input())
        for j in range(n):
            n1 = int(input())
            lista.append(n1)

        lista_sorteada = sorted(lista)

        for livro in lista_sorteada:

            print((4 - len(str(livro))) * '0' + str(livro))


except EOFError:
    pass

