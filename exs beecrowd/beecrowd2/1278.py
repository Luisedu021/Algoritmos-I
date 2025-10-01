
while True:
    Lista = []
    Lista_tamanhos = []
    n = int(input())
    if n == 0:
        break
    for c in range(n ):
        frase = str(input())
        frase_sem_ = frase.split()
        tamanho = len(frase)
        Lista_tamanhos.append(tamanho)

        Lista.append(frase)
    maximo = max(Lista_tamanhos)
    for k in range(len(Lista)):
        if maximo == len(Lista[k]):
            print(Lista[k])
        else:
            print(Lista[k].rstrip())

