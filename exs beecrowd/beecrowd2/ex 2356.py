try :
    while True:
        D = input()
        S = input()
        if S in D:
            print('Resistente')
        else:
            print('Nao resistente')

except EOFError:
    pass