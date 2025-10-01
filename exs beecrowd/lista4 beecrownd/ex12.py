is_sabre = False
l,c =map(int,input().split())

matriz = []

for i in range(l):
    linha = list(map(int,input().split()))
    matriz.append(linha)

for i,linha in enumerate(matriz):
    for j,coluna in enumerate(linha):
        if coluna == 42 and i + 1 <= l -1 and i - 1 >=0 and j + 1<= c -1 and j - 1 >= 0 :
            if matriz[i + 1][j] == 7  and matriz[i - 1][j] == 7 and matriz[i][j + 1 ] == 7 and matriz[i][j - 1] == 7  and matriz[i+1][j+1] == 7 and matriz[i+1][j-1] == 7 and matriz[i-1][j+1]== 7 and matriz[i-1][j-1] == 7 :
                print(i + 1,j + 1)
                is_sabre = True
if is_sabre == False:
    print('0 0')

