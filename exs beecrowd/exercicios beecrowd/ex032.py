ano = int(input('Digite um ano qualquer;'))
if ano%4==0 and ano%400==0 and ano%100 !=0:
    print('{} é ano bissexto'.format(ano))
else:
    print('{} não é ano bissexto'.format(ano))
