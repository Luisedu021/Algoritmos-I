#adicionando variáveis para os lados da forma geométrica
a,b,c = map(float,(input().split()))
#adicionando cores no terminal
cores = { 'limpa' : '\033[m',
          'azul' : '\033[34m',
          'amarelo' : '\033[1;33;40m',
          'verde' : '\033[1;32m'}
#adicionando as condicionais e satisfazendo a condição de existência de um triângulo
if a < b + c and b < a +c and c<a + b:
    p =a + b + c
    print(f'Perimetro ={cores['verde']}{p:.1f} \033[m')
else:
    At = ((a + b )*c )/2
    print(f'Area = {cores['azul']}{At:.1f}\033[m')
