n=int(input('Digite um número:'))

if n%2==0:
    print('\033[1;33m{}\033[m é um número par'.format(n))
else:
    print('\033[1;36m{}\033[m é um número ímpar'.format(n))
