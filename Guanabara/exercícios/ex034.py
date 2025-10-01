salario=float(input('Digite o valor de seu salário:'))
#variaveis de aumento
aumento = salario*1.1
aumento2=salario*1.15
#cores no terminal
cores = {'limpa':'\033[m ',
         'verde' : '\033[1;32m',
         'verde2' : '\033[7;32m'}
#condicionais
if salario >1250:
    print('Seu salário tera um {}aumento de 10%{},tornando o R${:.2f}'.format(cores['verde'],cores['limpa'],aumento))
else:
    print('Seu salário terá um{} aumento de 15%{},tornando o R${:.2f}'.format(cores['verde2'],cores['limpa'],aumento2,))
