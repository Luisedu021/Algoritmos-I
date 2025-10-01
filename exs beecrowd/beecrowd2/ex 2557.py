try:
    while True:
        letras = ['J','L','R']

        entrada = input().split('+')
        entrada1 = entrada[1].split('=')

        v1 = entrada[0]
        v2 = entrada1[0]
        v3 = entrada1[1]

        if v1 in letras:
            print(int(v3) - int(v2))
        elif v2 in letras:
            print(int(v3) - int(v1))
        elif v3 in letras:
            print(int(v1) + int(v2))
except EOFError:
    pass
