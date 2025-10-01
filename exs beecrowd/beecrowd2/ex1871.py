try:
    while True:
        n1,n2 = map(int,input().split())
        if n1 == 0 == n2:
            break
        soma = n1 + n2
        soma = str(soma)
        soma = soma.replace('0','')
        print(soma)
except EOFError:
    pass
