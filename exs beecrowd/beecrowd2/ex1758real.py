try:
    while True:

        n = int(input())
        for i in range(1,n+1,2):

                espaço2 = '*' * i
                cent = espaço2.center(n,' ')
                print(cent)
        cent3 = '*'.center(n, ' ')
        print(cent3)
        cent2 = '***'.center(n,' ')
        print(cent2)
        print()


except  EOFError:
    pass


