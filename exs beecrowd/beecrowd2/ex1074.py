ceven = codd = cpositive = cnegative = 0

n = int(input())
for c in range(0,n):
    n1 = int(input())

    if n1 == 0 :
            print('NULL')

    elif n1 % 2 == 0 :
        print('EVEN', end=' ')
        if n1 > 0 :
            print('POSITIVE')

        else:
            print('NEGATIVE')

    else:
        print('ODD',end = ' ')

        if n1 > 0:
            print('POSITIVE')

        else:
            print('NEGATIVE')



