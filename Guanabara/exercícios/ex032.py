#importação de datetime
import datetime
print('Verificador de ano bissexto')
#entrada do usuário e do ano desejado
ano = int(input('Digite um ano qualquer(Caso queira analisar o ano atual,clique em 0):'))
#adicionando uma lista de cores para usar no terminal
cores = {'limpa':'\033[m',
         'verde':'\033[1;32m',
         'azul':'\033[1;34m',
         'vermelho':'\033[1;31m'}
#condição caso o usuário queira o ano atual(ano será retirado do próprio pc)
#para que um ano seja bissexto é necessario que ele seja multiplo de 4 e não seja divisivel por 100 ou também ser divisivel por 400
if ano == 0:
    ano = datetime.date.today().year
    if ano % 4 ==0 and ano % 100 != 0 or ano % 400 ==0:
        print('O ano {} {}é bissexto\033[m'.format(ano,cores['verde']))
    else :
        print('O ano {} {}não é bissexto\033[m'.format(ano,cores['vermelho']))
#condição caso o usuário queira que o programa verifique se o ano desejado por ele é bissexto
elif ano != 0:
    if ano % 4 ==0 and ano % 100 != 0 or ano % 400 ==0:
        print('O ano {} {}é bissexto\033[m'.format(ano,cores['verde']))
    else :
        print('O ano {} {}não é bissexto\033[m'.format(ano,cores['vermelho']))












