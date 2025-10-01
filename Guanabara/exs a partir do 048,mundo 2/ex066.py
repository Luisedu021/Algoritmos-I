cont = soma =  0

while True:
    n = float(input('Digite um número:'))

    if n == 999:
        break
    cont += 1
    soma += n

print(f'Você digitou {cont} número e soma entre ele é: {soma}')