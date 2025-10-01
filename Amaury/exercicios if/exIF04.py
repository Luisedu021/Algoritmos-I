#atribuindo a variável de energia(e)
e=float(input('Digite o valor da energia em reais : '))
#atribuindo o salário de maria e joão
m=5000
j=2500
#atribuindo o valor da energia total de um mês
et =5/100*e
#porcentagem nova de energia dado o aumento mensal
en= 107/100*et
#diferença entre as energias mensais
eamais= en - et
#atribuindo váriaveis para o resto do sálario de maria e joão
rm= 90/100*m - 150
rj=2/3*j
#exibição do que foi pedido no exercício
print('O valor restante dos salarios de João e Maria respectivamente será de: {:.2f} e {:.2f} reais '.format(rj,rm))
print('Eles irão pagar nesse mês a quantia de {:.2f} reais  e no proximo mês {:.2f} reais \nAlém de pagarem {:.2f} reais a mais ' .format(et,en,eamais) )






