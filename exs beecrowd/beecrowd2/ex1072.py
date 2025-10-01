n = int(input())
cp = 0
cn = 0

for c in range(0,n):
        n1= int(input())
        if  0 <= n1 <= 20: cp += 1
        else: cn += 1


print(cp,'in')
print(cn,'out')
