inicial = float(input('Digite seu capital inicial: '))
taxa = float(input('Digite sua taxa anual: '))
anos = int(input('Digite o total de anos:'))

juros = inicial * taxa/100 * anos

montante = inicial + juros
print('O seu montante será de R$', montante)
