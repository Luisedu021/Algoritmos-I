num = [0,6 ,4,2,4,7,8,0,3,102]

num[6] = 10
print(num)
num.append(-29)
print(num)
num.sort()
print(num)
num.reverse()
print(num)
num.insert(0,20)
print(num)
num.pop(0)
print(num)
valores = list()
valores.append(10)
valores.append(20)
valores.append(30)
valores.append(40)

print('Os valores são',end = ' ')
for v in valores:
    if v != 40:
        print(v, end = ' ')
    else:
        print(v)

for c, v in enumerate(valores):
    print(f'Na posição {c+ 1} encontrei o valor {v}.')

a = [2,3,6,7,9]
b = a[:]
b[0] = 0
print(a)
print(b)