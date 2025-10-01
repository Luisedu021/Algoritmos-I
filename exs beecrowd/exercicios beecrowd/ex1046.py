a,b = map(int,input().split())
print('jdskldsjdsjj {}'.format('15 %'))
if a == b == 0 :
    print('O JOGO DUROU 24 HORA(S)')
else :
    if b > a:
        print('O JOGO DUROU {} HORA(S)'.format(b - a))
    else:
        print('O JOGO DUROU {} HORA(S)'.format( 24 - a + b ))