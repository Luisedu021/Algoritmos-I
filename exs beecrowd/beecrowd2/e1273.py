n = int(input())
lista = []
lista_frases = []
for i in range(n):
    frase = input()
    lista.append(len(frase))
    lista_frases.append(frase)

for j in range(len(lista)):
    maximo = max(lista)
    if lista[j] != maximo:
        frasecerta = lista_frases[j].rjust(maximo + len(lista_frases[j]))
        print(frasecerta)
    else:
        print(lista_frases[j])