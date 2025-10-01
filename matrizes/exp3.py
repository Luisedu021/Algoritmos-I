n = int(input())
def eh_primo(n):
    cont = 0
    for i in range(2,n):

        if n % i == 0:
            cont += 1
    if cont > 0:
        return False
    else:
        return True


def verifica_especial(n):
    ver = False
    if n > 0 and type(n) == int:

        if (n % 3 == 0 or n % 5 == 0) and not (n % 3 == 0 and n % 5 == 0):

            if eh_primo(n) == True:

                    ver = False
            else:
                    ver = True

    return ver

if verifica_especial(n) == True:
    print('Número especial')
else:
    print('Número comum')
