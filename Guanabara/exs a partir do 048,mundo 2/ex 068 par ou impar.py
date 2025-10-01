import random as r
cores = {'limpa': '\033[m',
         'verde' : '\033[1;32m',
        'vermelho': '\033[1;31m' }


print(f'{cores['verde']} Par ou Impar{cores['limpa']}')
cont = 0
while True:
    n = r.randint(1, 10)
    print(n)
    soma = n
    j = input('Par ou Impar?[P/I]')
    nj = int(input('Digite um valor de 1 a 10'))
    soma += nj
    if soma % 2 == 0 and j == 'P':
        print(f'Você ganhou,parabéns,voce escolheu {nj},o computador escolheu {n} e {soma} é par')
        cont += 1
    elif soma % 2 == 1 and j == 'I':
        print(f'Você ganhou,parabéns,voce escolheu {nj},o computador escolheu {n} e {soma} é ímpar')
        cont += 1
    else:
        print(f'Você perdeu, voce escolheu {nj},o computador escolheu {n}')
        print(f'Você ganhou {cont} vezes.')
        break





