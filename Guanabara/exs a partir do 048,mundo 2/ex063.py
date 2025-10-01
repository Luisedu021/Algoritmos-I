print('FIBONACCI')
n = int(input())
sequencia = [0,1]
if n <= 2:
    for j in range(0,n ):
        print(sequencia[j])


else:
    print('Sequência: (0,1, ',end = '' )
    for i in range(2,n ):
        sequencia.append(sequencia[i-1] + sequencia[i-2])
        if i < n-1:
            print(sequencia[i],end = ', ')
        else:
            print('{})'.format(sequencia[i]))

