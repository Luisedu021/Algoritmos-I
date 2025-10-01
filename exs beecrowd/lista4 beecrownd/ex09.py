from sympy.printing.aesaracode import true_divide

n = int(input())
lista = []

for i in range(n):
    ver,num = map(int,input().split())
    if ver == 1:
        lista.append(num)
    else:
        lista.pop(lista.index(num))
print(lista)
