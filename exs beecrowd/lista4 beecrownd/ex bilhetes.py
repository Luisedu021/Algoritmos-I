while True:
    nb,np = map(int,input().split())
    if nb == 0 and np == 0:
        break

    numeros = input().split()
    numeros1 = set(numeros)
    rep = 0
    rep1 = 0
    for numero in numeros1:
        rep = numeros.count(numero)
        if rep > 1:
            rep1 += 1
    print(rep1)