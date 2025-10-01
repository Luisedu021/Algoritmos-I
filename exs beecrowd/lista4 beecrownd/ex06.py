n =int(input())

for i in range(n):
    st1 , st2 = input().split()
    stnova = st1[-len(st2):]
    if stnova == st2:
        print('encaixa')
    else:
        print('nao encaixa')

