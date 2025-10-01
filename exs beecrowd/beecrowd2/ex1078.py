N = int(input())

contador = 1
for i in range(1,11):

    tabuada = contador * N
    contador += 1
    print('{} x {} = {}'.format(i,N,tabuada))
