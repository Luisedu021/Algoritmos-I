c = 0
media = 0
for r in range(0,6):
    n = float(input())
    if n > 0 :
        c +=  1
        media += n
c= round(c)
print('{} valores positivos'.format(c))

print('{:.1f}'.format(media / c))