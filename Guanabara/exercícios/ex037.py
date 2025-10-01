print('Conversor de bases numéricas')
número = int(input('Digite um número inteiro:'))
condição = int(input('Se quiser converter para binário digite:\n[1]: para binário\n[2]: para octal\n[3]: para hexadecimal: '))
binario = bin(número)
binario  = binario[2:]
hexadecimal = hex(número)
hexadecimal =hexadecimal[2:]
octal = oct(número)
octal = octal[2:]

if condição == 1:
    print('Seu número {} em binário é {}'.format(número,binario))
elif condição == 2 :
    print('Seu número {} em octal é {}'.format(número,octal))
elif condição == 3  :
    print('Seu número {} em hexadecimal é {} '.format(número,hexadecimal))
else:
    print('Opção inválida.Tente novamente!')


