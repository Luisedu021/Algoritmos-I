n, k = map(int, input().split()) # vai receber n e k
limites = list(map(int,input().split())) # vai ler os limites
posicao = [] #posicao onde cada particula vai parar

for i in range(n):
    fase = limites[i]
    j = i

    while True :
        if fase > limites[j]:
            posicao.append(i + 1)
            break
        else:
            fase += k
            j = (j + 1) % n # vai para proxima porta
print(posicao)
