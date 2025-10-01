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
lista.sort()
print('-=' * 30)
print(f'Você digitou os valores {lista}')