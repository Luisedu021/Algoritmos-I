#aplicando a entrada do usuário em segundos
ts=int(input())
#tendo em vista que 1 hora = 60 min e 1 min=60 s,se dividirmos por 60*60=3600 que será o valor das horas
th=ts//3600
#realizando o resto pela função de %
resto=ts%3600
#realizando o mesmo raciocínio de cima
tm=resto//60
resto2=resto%60
ts=resto2
#aplicando do jeito que o comando da questão pedia
print('{}:{}:{}'.format(th,tm,ts))

