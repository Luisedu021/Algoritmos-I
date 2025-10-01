frase = input()
vogais  = ['a', 'e', 'i', 'o', 'u']
frase_nova = []
frase_nova_invertida = []
for j in range(len(frase)):
    if frase[j] in vogais:
        frase_nova.append(frase[j])

for i in range(len(frase_nova) - 1,- 1,- 1):
    frase_nova_invertida.append(frase_nova[i])

if frase_nova_invertida == frase_nova:
    print('S')
else:
    print('N')
