#entrada do usuário
diainicio = input()
inicio = input()
diafim = input()
fim = input()

#formatação para pegar o dia que começa
diainicio = diainicio.split()

diainicio = int(diainicio[1])

 #organizando as horas,minutos e segundos que começa o evento
inicio = inicio.split()

iniciohora = int(inicio [0])
iniciominuto = int(inicio[2])
iniciosegundo = int(inicio [4])

#formatando para pegar o dia que termina
diafim = diafim.split()

diafim = int(diafim[1])

#organizando o fim em horas,minutos e segundos
fim = fim.split()

fimhora = int(fim[0])
fimminuto = int(fim[2])
fimsegundo = int(fim[4])
print(fimsegundo)
#adicionando as condicionais

diferenca_segundo = fimsegundo - iniciosegundo

#primeira condicional caso de tudo certo :)
if fimhora >= iniciohora:
        diferenca_dias = diafim - diainicio
        print('{} dia(s)'.format(diferenca_dias))
        diferenca_hora = fimhora - iniciohora
        print('{} hora(s)'.format(diferenca_hora))

        if fimminuto >= iniciominuto:

                if fimsegundo > iniciosegundo:

                    diferenca_minuto = fimminuto - iniciominuto
                    diferenca_segundo = fimsegundo - iniciosegundo
                    print('{} minuto(s)'.format(diferenca_minuto))

                elif fimsegundo < iniciosegundo:
                    diferenca_minuto = fimminuto - iniciominuto - 1
                    diferenca_segundo = 60 - iniciosegundo + fimsegundo
                    print('{} segundo(s)'.format(diferenca_segundo))


        elif fimminuto < iniciominuto:
            diferenca_minuto = 60 - iniciominuto + fimminuto
            print('{} minuto(s)'.format(diferenca_minuto))
            print('{} segundo(s)'.format(diferenca_segundo))

#caso fimhora < fiminicio,ou seja,ela começa as  7  e termina as 3
elif fimhora < iniciohora:

    diferenca_dias = diafim - diainicio - 1
    print('{} dia(s)'.format(diferenca_dias))

    diferenca_hora = 24 - iniciohora + fimhora
    print('{} hora(s)'.format(diferenca_hora))

    if fimminuto >=  iniciominuto:
        diferenca_minuto = fimminuto - iniciominuto
        if fimsegundo  >=  iniciosegundo:
            diferenca_segundo = iniciosegundo + fimsegundo
            print('{} minuto(s)'.format(diferenca_minuto ))
            print('{} segundo(s)'.format(diferenca_segundo))

        elif fimsegundo < iniciosegundo:
            diferenca_segundo = 60 - iniciosegundo  + fimsegundo
            print('{} minuto(s)'.format(diferenca_minuto))
            print('{} segundo(s)'.format(diferenca_segundo))




    elif iniciominuto > fimminuto:
        diferenca_minuto =  60 - iniciominuto + fimminuto

        if fimsegundo >= iniciosegundo:
            diferenca_segundo = iniciosegundo + fimsegundo
            print('{} minuto(s)'.format(diferenca_minuto))
            print('{} segundo(s)'.format(diferenca_segundo))

        elif fimsegundo < iniciosegundo:
            diferenca_segundo = 60 - iniciosegundo + fimsegundo
            print('{} minuto(s)'.format(diferenca_minuto))
            print('{} segundo(s)'.format(diferenca_segundo))


























