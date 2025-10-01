#adicionando variáveis de tempo para a entrada do usuário
h1,m1,h2,m2 = map(int,input().split())
#variaveis que usarei
horas = h2 -h1
horas2 = 24 - h1 + h2
horas3 = 24 -h1 + h2 -1
minutos = m2 -m1
minutos2 = 60 - m1 + m2
#primeira condição caso a segunda hora seja maior que a primeira
if h2 > h1:
#se ela for maior juntamente com a seguna minutagem maior usaremos o simples
    if m2> m1:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas,minutos))

        '''se a segunda minutagem for menor,significa que teremos de subtrair 1 hora,exemplo: 
        comecei as 2 das 20 e terminei as 3 das 10,em tese eu teria 1 hora pela logica,mas como n completou a hora nas minutagens,tenho que subtrair 1 '''

    elif m2 < m1:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas- 1,minutos2))
    elif m2 == m1:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas+ 1,0))
elif h2 ==h1:
    if m2 > m1:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
    elif m2 < m1:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas2 -1, minutos2))
    elif m2 == m1:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas2, minutos))
elif h2 <h1:
    if m2 > m1:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas2, minutos))
    elif m2 < m1:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas2 - 1 , minutos2))
    elif m2 == m1:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas2, minutos2))
