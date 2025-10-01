n = int(input('Digite um número:'))
c = n
f = 1

while c >0:

    if c > 1:
        print('{}'.format(c),end = ' x ')
    else:
        print('{}'.format(c),end = ' = ')
    f = f * c

    c -= 1
print('{}'.format(f))

