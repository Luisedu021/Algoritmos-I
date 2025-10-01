numeros = (int(input('Digite um numero: ')),
           int(input('Digite outro numero: ')),
           int(input('Digite mais um numero: ')),
           int(input('Digite o ultimo numero: ')),
           )


cont = 0
posicao = ''
numeros_pares = ' '
for i in range(0,len(numeros)):
    if numeros[i] == 9:
        cont += 1
    if numeros[i] == 3:
         posicao = posicao  + str(i)
    if numeros[i] % 2 == 0:
        numeros_pares += str(numeros[i]) + ' '
if len(posicao) > 0:
    print(f'A posição do valor 3 é: {int(posicao[0]) + 1}')
else:
    print('O valor 3 não apareceu')

print(f'Temos ao todo {cont} números 9')

print(f'Números pares: {numeros_pares}')