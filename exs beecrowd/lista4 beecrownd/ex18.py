while True:
    try:
        angulo = int(input())
        if angulo < 90 or angulo == 360:
            print('Bom Dia!!')
        elif angulo >= 90 and angulo < 180:
            print('Boa Tarde!!')
        elif angulo >= 180 and angulo < 270:
            print('Boa Noite!!')
        elif angulo >= 270 and angulo < 360:
            print("De Madrugada!!")
    except EOFError:
        break

