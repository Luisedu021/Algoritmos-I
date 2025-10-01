nome  = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

nome_c = nome + ' '  + sobrenome

nome_M = nome_c.upper()
nome_m = nome_c.lower()

print('Seu nome completo em maiúsculas fica: {}.'.format(nome_M),end = ' ')
print('Seu nome completo em minúsculas fica: {}'.format(nome_m))

nome_c = nome_c.replace(' ', '')
tamanho = len(nome_c)

print('O tanto de letras que seu nome possui é: {}'.format(tamanho))

