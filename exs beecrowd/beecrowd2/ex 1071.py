n = int(input())
n2 = int(input())
contador = 0
if n2 < n :
    for c in range(n - 1  ,n2, -1):
        if c % 2 != 0 :

            contador += c
else:
    for c in range(n+1,n2,):
        if c % 2 != 0 :

            contador += c

print(contador)
