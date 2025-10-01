#entrada do usuário
N = int(input())
#fazendo um algoritmo que ao ver o valor da entrada,ele  faz N vezes a média ponderada
for i in range(0,N):
    n,n1,n2 = map(float,input().split())
    media  = (2 * n + n1 * 3 + n2 * 5 )/10
    print('{:.1f}'.format(media))
