# Problema 6: Quantidade de números pares e ímpares pode ser feito sem o uso de vetores
def pares_impares(n):
    pares = 0
    impares = 0
    for i in range(n):
        valor = int(input())
        if valor % 2 == 0:
            pares += 1
        else:
            impares += 1
    return f'São pares: {pares}, impares: {impares}'

# Problema 7: Inventário e média dos estoques (com/sem vetor)
def inventario_produtos(n):
    codigos_produtos = []
    cod_prod_abaixo = []
    produtos_est= []
    soma = 0
    for i in range(n):
        estoque  = int(input())
        cod = int(input())
        produtos_est.append(estoque)
        codigos_produtos.append(cod)
        soma += estoque
    media  = soma /n

    for indice,num in enumerate(produtos_est):
        if num < media:
            cod_prod_abaixo.append(codigos_produtos[indice])

    return f'A média é {media},os produtos{codigos_produtos} abaixo da média são: {cod_prod_abaixo}.'

