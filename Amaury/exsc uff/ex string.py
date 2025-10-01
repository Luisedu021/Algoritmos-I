nome = input('Entre com um nome completo:').strip().upper()


iniciais = ' ' # marca a variável iniciais como uma variavel para guardar strings

inicio = 0 # contador usado para mexer nas strings
fim = nome.find(' ', inicio )

#estrutura de rep para achar os nomes iniciais e o último nome
while fim != -1 :
    iniciais += nome[inicio] + '. '
    inicio = fim + 1
    fim = nome.find(' ',inicio)

#achar o último nome com formatação de string
ultimo  = nome[inicio: ]

#saída desejado pelo problema
print('Seu nome de citação é : {},{}'.format(ultimo,iniciais))





#outro met.
"""ultimo = nome[espacos:]
print(ultimo)
print('Oisss')
contador = nome.count(' ')

iniciais = nome.split()
iniciais1 = iniciais[0]
iniciais1 = iniciais1[0]
print(iniciais1)
iniciais2 = iniciais[1]
iniciais2 = iniciais2[0]
ultimos  = iniciais[contador ]
print(iniciais1,iniciais2,ultimos)
print('{},{}.{}.'.format(ultimos.upper(),iniciais1.upper(),iniciais2.upper()))
"""
