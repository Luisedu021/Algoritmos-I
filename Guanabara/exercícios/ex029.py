from time import sleep
print('Verificador de infração no trânsito'.upper())
print('O limitador de velocidade é de 80km/h')
v=int(input('Digite o valor de sua velocidade em km/h:'))
vex=v-80 #valor excedido
valor=vex*7
#fazendo uma lista de cores para usar
cores = {'limpa':'\033[m',
    'pretoebranco':'\033[7:30m',
        'vermelho':'\033[1:31m',
            'verde':'\033[1:32m'}
print('PROCESSANDO...')
sleep(1)
if v>80 :
    print ('{}VOCE FOI MULTADO!!\033[m \nSua multa será de R$ {} reais \nVoce excedeu {} km/h  '.format(cores['vermelho'],valor,vex))
else:
    print('{}PARABÉNS! \033[m\nVoce está  a {}km/h,logo está no limite de velocidade'.format(cores['verde'],v))
