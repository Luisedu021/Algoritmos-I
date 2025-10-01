numeros = ['zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez']
entrada = int(input())
numeros_decimais = ['vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']

if entrada < 20 :
    if entrada == 0 :
        print('zero')
    elif entrada == 1 :
        print('um')
    elif entrada == 2 :
        print('dois')
    elif entrada == 3 :
        print('três')
    elif entrada == 4 :
        print('quatro')
    elif entrada == 5 :
        print('cinco')
    elif entrada == 6 :
        print('seis')
    elif entrada == 7 :
        print('sete')
    elif entrada == 8 :
        print('oito')
    elif entrada == 9 :
        print('nove')
    elif entrada == 10 :
        print('dez')
    elif entrada == 11 :
        print('onze')
    elif entrada == 12 :
        print('doze')
    elif entrada == 13 :
        print('treze')
    elif entrada == 14 :
        print('quatorze')
    elif entrada == 15 :
        print('quinze')
    elif entrada == 16 :
        print('dezesseis')
    elif entrada == 17 :
        print('dezessete')
    elif entrada == 18 :
        print('dezoito')
    elif entrada == 19 :
        print('dezenove')
else:
    entrada = str(entrada)
    x = list(entrada)

    for i in range(0,1):

        if x[0] == '2':
            print('vinte',end = ' ')

        elif x[0] == '3':
            print('trinta',end = ' ')
        elif x[0] == '4':
            print('quarenta',end = ' ')
        elif x[0] == '5':
            print('cinquenta',end = ' ')
        elif x[0] == '6':
            print('sessenta',end = ' ')
        elif x[0] == '7':
            print('setenta',end = ' ')
        elif x[0] == '8':
            print('oitenta',end = ' ')
        elif x[0] == '9':
            print('noventa',end = ' ')

    if x[1] == '1':
        print('e um ')
    elif x[1] == '2':
        print('e dois')
    elif x[1] == '3':
        print('e três')
    elif x[1] == '4':
        print('e quatro')
    elif x[1] == '5':
        print('e cinco')
    elif x[1] == '6':
        print('e seis')
    elif x[1] == '7':
        print('e sete')
    elif x[1] == '8':
        print('e oito')
    elif x[1] == '9':
        print('e nove')






