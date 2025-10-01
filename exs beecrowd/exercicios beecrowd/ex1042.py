#entrada de usuário e dividindo a as variaveis
n1,n2,n3 = map(int,input().split())
#aplicando as condicionais na raça mesmo
if n1 < n2<n3 :
    print(n1)
    print(n2)
    print(n3)
elif n1 <n3<n2:
    print(n1)
    print(n3)
    print(n2)
elif n2<n3<n1:
    print(n2)
    print(n3)
    print(n1)
elif n2<n1<n3:
    print(n2)
    print(n1)
    print(n3)
elif n3<n1<n2:
    print(n3)
    print(n1)
    print(n2)
elif n3<n2<n1:
    print(n3)
    print(n2)
    print(n1)
print()#linha em branco
print(n1)
print(n2)
print(n3)
