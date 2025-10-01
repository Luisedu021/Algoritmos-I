frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split(' ')
juntas = ''.join(palavras)
inverso = ' '

for i in range(len(juntas)- 1,-1,-1):
    inverso += juntas[i]

print(inverso)
print(juntas)
if inverso == juntas:
    print('É palíndromo')
else:
    print('Não é palíndromo')

