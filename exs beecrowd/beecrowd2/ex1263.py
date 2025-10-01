def remover_rep(lista):
    if not lista:
        return []

try:
    while True:
        lista_letras = []
        lista_letras_repeticoes = []
        frase = input()
        frase = frase.lower().split()
        for j in range(len(frase)):

            lista_letras.append(frase[j][0])

        for i in range (len(lista_letras)):
            if i + 1 < len(lista_letras):
                 if lista_letras[i]  == lista_letras[i + 1]:
                     lista_letras_repeticoes.append(lista_letras[i])
        nova_lista = [lista[0]]
        lista_letras_semrep = list(set(lista_letras_repeticoes))
        print(lista_letras)
        print(lista_letras_repeticoes)
        print(lista_letras_semrep)










except EOFError:
    pass
