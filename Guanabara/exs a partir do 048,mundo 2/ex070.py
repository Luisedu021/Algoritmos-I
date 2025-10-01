produtos = []
precos = []
total = produtos1000 =  0

while True:
    produto = input('Nome do produto: ')
    preco =  int(input('Preço: R$'))
    if preco > 1000:
        produtos1000 += 1
    total += preco
    produtos.append(produto)
    precos.append(preco)
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N]').strip().upper()[0]
    if continuar == 'N':
        break

produtobarato = min(precos)


for j in range(len(precos)):
    if precos[j] == produtobarato:
        posicaobarato = j
print()
print('-' * 30)
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {produtos1000} produtos  custando mais de R$ 1000.00')
print(f'O produto mais barato foi {produtos[posicaobarato]} que custa R$ {produtobarato:.2f}')
print('-' * 30)