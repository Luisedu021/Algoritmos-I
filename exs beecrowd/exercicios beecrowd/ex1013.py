#adicionando as variáveis e e as transformando em inteiros
a,b,c = map(int,input().split(" "))
#aplicando as fórmulas
maiorab=((a+b+ abs(a-b))/2)
#aplicando as possibilidades caso  uma variável seja maior q outra

if maiorab > c:
     print('{} eh o maior'.format(maiorab))
else:
       print('{} eh o maior'.format(c))


