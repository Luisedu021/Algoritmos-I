
while True:
        cont = 0
        frase = input()
        if frase[0] == 'R':
            cont += 1
        cont2 = frase.count('W')
        if frase[len(frase) - 1 ] == 'R':
            cont += 1

        print(cont + cont2)
