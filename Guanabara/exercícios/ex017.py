from math import hypot
print('Relação pitagórica')
cat1=(input('Digite o nome de um cateto:'))
cat1f=float(cat1)
cat2=(input('Digite o nome do segundo cateto:'))
cat2f=float(cat2)
hip=hypot(cat1f,cat2f)

print('A raiz quadrada da soma entre o quadrado dos catetos resulta na hipotenusa,portanto a hipotenusa é {:.2f}'.format(hip))
