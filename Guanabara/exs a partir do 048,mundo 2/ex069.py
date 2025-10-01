print('-'*40)
print('CADASTRO DE PESSOAS')

cont18 = 0
cont20 = 0
conthomem= 0

while True:
    sexo = 's'
    print('-'*40)
    idade = int(input('Digite sua idade: '))

    while sexo != 'F' and sexo != 'M':
        sexo = input('Digite seu sexo (M/F): ').upper()[0]

    if sexo == 'M':
        conthomem += 1
    elif sexo == 'F':
        if idade < 20:
            cont20+= 1


    if idade > 18 :
        cont18+= 1
    verificador = ''
    while verificador != 'N' or verificador != 'S':
        print('-' * 40)
        verificador = input('Deseja continuar? [S/N] ').upper()[0]

        if verificador == 'N' or verificador == 'S':
            break

    if verificador == 'N':
        break



print('-' * 40)
print(f'Total de pessoas com mais de 18 anos: {cont18}')
print(f'Ao todo temos {conthomem} homens cadastrados')
print(f'E temos {cont20} mulheres com menos de 20 anos.')
