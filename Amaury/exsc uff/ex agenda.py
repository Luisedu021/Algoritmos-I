for hora in range(24):
    for minuto in range(0,60,15):
        if hora <= 12:
            if hora < 10:
                print( '0' + str(hora) + ':' + str(minuto) + ' AM')
            else:
                print( str(hora) + ':' + str(minuto) + ' AM')
        else :
            print( str(hora) + ':' + str(minuto) + ' PM')
