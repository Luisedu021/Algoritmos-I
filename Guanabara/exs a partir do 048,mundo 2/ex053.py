#entrada do usuário e formatando a frase para ela ficar junta e em letra maiúscula
frase = str(input('Digite uma frase: ')).strip().upper()
#divisão das frases
frase = frase.split()
#junção das frases
frase = ''.join(frase)

#contador para comparar se é palíndromo ou não
contador = 0
#variável para saber o tamanho da palavras
tamanho = len(frase)
#para verificar se é palindromo,basta chegar o primeiro termo com o último sucessivamente por meio de uma est de rep. for
for i in range(0,tamanho //2 ):
    if frase[i] == frase[tamanho -contador - 1]:

        contador += 1


if contador  == tamanho //2 :
    print('É palíndromo')
else:
    print('Não é palíndromo')
