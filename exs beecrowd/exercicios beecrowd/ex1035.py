A,B,C,D = map(int,input().split())
v1=bool(B>C and D >A  and C>0 and D>0 )
v2= bool((C+D) > (A+B))
v3=bool(A%2 ==0)
if not (v1 and v2 and v3):
    print('Valores nao aceitos')
else:
        print('Valores aceitos')
