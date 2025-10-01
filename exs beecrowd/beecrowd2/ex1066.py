contadorp = contadorn = contador2= contador1 = 0

for c in range(0,5):
    n = int(input())
    if n % 2 == 0 :
        contador2 += 1
    else:
        contador1 += 1

    if n > 0:
        contadorp += 1
    elif n < 0:
        contadorn += 1

print(contador2,'valor(es) par(es)')
print(contador1,'valor(es) impar(es)')
print(contadorp,'valor(es) positivo(s)')
print(contadorn,'valor(es) negativo(s)')
