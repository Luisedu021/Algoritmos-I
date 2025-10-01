#entrada do usuário
n = int(input())
#contador para cada animal testado

contadorc = 0
contadorr = 0
contadors = 0

#estrutura de rep para contar os animais

for i in range(0,n):

#entrada do número de animais  e formatação para manipular os valores
        entrada  = (input())
        entrada = entrada.strip().split()
        qntd = int(entrada[0])

#condicionais para contar cada animal
        if entrada[1] == 'C' :
                    contadorc = contadorc + qntd
        elif entrada[1] == 'R' :
            contadorr +=  qntd
        else:
            contadors += qntd

#total de cobaias
total = contadorc + contadorr + contadors
#saída do total de cobaias e especificação de cada uma dessas

print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(contadorc))
print('Total de ratos: {}'.format(contadorr))
print('Total de sapos: {}'.format(contadors))

#saída do percentual

print('Percentual de coelhos: {:.2f} %'.format(contadorc / total * 100))
print('Percentual de ratos: {:.2f} %'.format(contadorr / total * 100))
print('Percentual de sapos: {:.2f} %'.format(contadors / total * 100))