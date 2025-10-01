n = int(input('Digite um número:'))
cont = 0
for c in range(1,n + 1 ):

    if n % c  == 0:
        print('{}{}\033[m'.format('\033[34m',c),end = ' ')
        cont += 1

    else:
        print(c,end = ' ')

if cont >  2:
    print('\nO número {} foi divisível {} vezes'.format(n,cont))
    print('E por isso,ele não é primo')

else:
    print('\nO seu número não é divisível por nenhum número além dele mesmo e 1 \nPor isso,ele é primo!')
