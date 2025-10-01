expressao = input('Digite uma expressão: ')
expressao1 = []
for letra in expressao:
    expressao1.append(letra)

v1 =expressao.count('(')
v2 = expressao.count(')')
cont = 0
if v1 == v2:
    for i in range(v1):
        comp = expressao1.index('(')
        comp2 =expressao1.index(')')
        if comp < comp2:
            cont += 0
        else:
            cont += 1
        expressao1.remove('(')
        expressao1.remove(')')
    if cont == 0:
        print('Expressão válida!')
    else:
        print('Expressão inválida!')
else:
    print('Sua expressão é inválida!')

