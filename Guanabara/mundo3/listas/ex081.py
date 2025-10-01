lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado!Não vou adicionar...')

    verificacao = input('Deseja continuar?[S/N]')
    if verificacao.upper()[0] == 'N':
        break

print(f'Foram digitados {len(lista)} números.')
lista.sort()
lista.reverse()
print(f'Lista ordenada em ordem decrescente: {lista}')

if 5 in lista:
    print('O valor 5 aparece na lista')
else:
    print('O valor 5 não aparece na lista')
    