n = int(input('Digite um número para ver sua tabuada:'))
tabuada = 1
for c in range (1,11):
    tabuada  = n * c
    print('{} x {} = {}'.format(n,c,tabuada))
