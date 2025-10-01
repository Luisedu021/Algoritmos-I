#entrada do usuário

valor = float(input('Digite o valor em reais: '))

cotacao = float(input('Digite o valor da cotação em dolar para reais: '))

#criação de variáveis

valor_emdolar = valor / cotacao

#saída
print('O valor em dolares da sua quantidade é de ${} doláres'.format(valor_emdolar))

