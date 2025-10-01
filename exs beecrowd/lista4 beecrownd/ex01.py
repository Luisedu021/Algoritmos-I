n1,n2,n3 = map(int,input().split())
maior = (n1+ n2 + abs(n1-n2)) /2

if n3 > maior:
    maior = n3
print(f'{maior:.0f} eh o maior')
