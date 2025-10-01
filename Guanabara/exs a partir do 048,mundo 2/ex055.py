comparador = 0
Lista = []
for i in range(0,5):
    peso = float(input('Peso da {}ª pessoa:'.format(i+1)))
    Lista.append(peso)

menor = 0
maior = 0


maximo = max(Lista)
mínimo = min(Lista)

for i in range(0,5):

    if Lista[i] == maximo :
        maior = i
    elif Lista[i] == mínimo :
        menor = i


print('O maior peso lido foi de {}Kg'.format(maximo))
print('O menor peso lido foi de {}Kg'.format(mínimo))