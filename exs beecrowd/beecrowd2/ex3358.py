n = int(input())

lista = ['a','e','i','o','u']
frase = ''
verificador = '000'

nomes = []
facilidades = []



for i in range(n):
    nome = input()
    nomes.append(nome)

    nome = nome.lower()
    for j in range(len(nome) ):
        if nome[j] in lista:
            frase += '1'
        else:
            frase += '0'
    if '000' in frase or '0000' in frase:
        facilidades.append('não eh facil')
    else:
        facilidades.append('eh facil')

    frase = ''

for n in range(len(facilidades) ):
    print('{} {}'.format(nomes[n],facilidades[n]))
