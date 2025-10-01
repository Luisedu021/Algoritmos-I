#valores de entrada
valor = (input('Qual o valor da casa?'))
salario =(input('Qual o salário mensal?'))
anos = int(input('Em quantos anos vai pagar?'))
#transformando o valor em float caso o usuario escreva R$
valor = valor.replace('R$','')
valor = float(valor)
#mesmo raciocinio anterior
salario = salario.replace('R$', " ")
salario = float(salario)
#adicionando a prestação
prestação = valor / (anos * 12)

minimo = salario * 30/100
#adicionando condições do desafio
if prestação <= minimo :
    print('Para pegar uma casa de {} em {} anos a prestação será de R${:.2f}'.format(valor,anos,prestação))
    print('Emprestimo aprovado!')
else :
    print('Para pegar uma casa de {} em {} anos a prestação será de R${:.2f}'.format(valor, anos, prestação))
    print('Emprestime reprovado!')