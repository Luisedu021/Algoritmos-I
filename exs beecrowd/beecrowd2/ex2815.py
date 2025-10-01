frase = input().split()

for j in range(len(frase)):

    if j == (len(frase) - 1):

        if frase[j] [0:2]== frase[j][2:4]:
            print(frase[j][2:],end ='')
        else:
            print(frase[j],end ='')

    else:

        if frase[j] [0:2]== frase[j][2:4]:
            print(frase[j][2:],end =' ')
        else:
            print(frase[j],end =' ')