n = int(input())

for c in range(n):
    v1,v2 = input().split()

    if v1 == 'spock':

        if v2 == 'spock':
            print('empate')

        if v2 == 'tesoura':
            print('rajesh')

        if v2 == 'pedra':
            print('rajesh')

        if v2 == 'papel':
            print('sheldon')

        if v2 == 'lagarto':
            print('sheldon')

    if v1 == 'tesoura':

        if v2 == 'tesoura':
            print('empate')

        elif  v2 == 'spock':
            print('sheldon')

        elif  v2 == 'pedra':
            print('sheldon')

        elif v2 == 'papel':
            print('rajesh')

        elif v2 == 'lagarto':
            print('rajesh')

    if v1 == 'pedra':

        if v2 == 'pedra':
            print('empate')

        elif v2 == 'spock':
            print('sheldon')

        elif v2 == 'tesoura':
            print('rajesh')

        elif v2 == 'papel':
            print('sheldon')

        elif v2 == 'lagarto':
            print('rajesh')

    if v1 == 'lagarto':

        if v2 == 'lagarto':
            print('empate')

        elif v2 == 'spock':
            print('rajesh')

        elif v2 == 'tesoura':
            print('sheldon')

        elif v2 == 'papel':
            print('rajesh')

        elif v2 == 'pedra':
            print('sheldon')

    if v1 == 'papel':

        if v2 == 'papel':
            print('empate')

        elif v2 == 'spock':
            print('rajesh')

        elif v2 == 'tesoura':
            print('sheldon')

        elif v2 == 'lagarto':
            print('sheldon')

        elif v2 == 'pedra':
            print('rajesh')

