from math import sqrt
x1,x2,y1,y2 = map(float,input("Me informe o x1,x2,y1,y2:").split())
d = sqrt( ( x2 - x1 )** 2 + ( y2 - y1 ) ** 2 )
print('A distância entre esses pontos é: {:.2f}'.format(d))
