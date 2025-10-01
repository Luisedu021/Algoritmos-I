#ENTRADA DO NUMERO DE VEZES DO LOOP
n = int(input())
#ACUMULADOR PARA VERIFICAR SE 'ENCAIXA OU N'
ac = 0
#VETORES PARA ARMAZENANTO DE STRINGS
listaA = []
listaB = []
#LOOP
for c in range(n):

    a,b = input().split()

    tamanhoa = len(a)
    tamanhob = len(b)
    #condição de existencia do codigo para comparar
    if tamanhoa >= tamanhob:
        #add as strings
        for j in range((abs(tamanhoa - tamanhob)),tamanhoa):

            listaA.append(int(a[j]))

        for i in range(tamanhob):

            listaB.append(int(b[i]))

            #verificando se são diferentes,e caso sejam,soma um no acumulador
            if listaA[i] != listaB[i]:

                ac += 1

        if ac == 0 :
            print('encaixa')
        else:
            print('nao encaixa')
    else:
        print('nao encaixa')
    #zerando variaveis caso ocorra outro loop
    ac = 0
    listaB = []
    listaA = []





