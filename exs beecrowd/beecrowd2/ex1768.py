try:
    while True:
        n = int(input())
        for j in range(1,n + 1,2):
            if n % 2 != 0:
                espacos = (n - j )/2
            else:
                espacos = (n - 1 -j) /2
            print(int(espacos) * ' ' + '*' * j)

        print(int((n - 1 )/ 2) * ' ' + '*' ) if n % 2 != 0 else int((n - 2) / 2) * ' ' + '*'
        print(int((n - 3) / 2) * ' ' + '***') if n % 2 != 0 else int((n - 4) / 2) * ' ' + '***'
        print()

except EOFError:
    pass
