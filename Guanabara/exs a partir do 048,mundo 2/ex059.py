n = 0
while n != 5:
    n1,n2 = map(float,input('Digite dois valores:').split())
    n = int(input('Digite um valor: \n[1]somar \n[2]multiplicar \n[3]maior \n[4]novos números \n[5]sair do programa :'))
    if n == 1:
        print('A soma é de {}'.format(n1 + n2))
    elif n == 2 :
        print('A multiplicação é de {}'.format(n1 * n2))
    elif n == 3:
        print('O maior número é o {}'.format(n1 if n1 > n2 else n2))

