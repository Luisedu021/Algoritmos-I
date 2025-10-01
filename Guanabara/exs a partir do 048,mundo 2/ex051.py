print('{}PROGRESSÃO ARITMÉTICA\033[m'.format('\033[1;33m'))
n = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
soma = n

décimo = n + (10 -1 ) * r
for c in range(n,décimo + r ,r):
    print(c,end = ' ')
    soma += c

print("\nA soma entre os dez primeiros termos é de {}".format(soma))


