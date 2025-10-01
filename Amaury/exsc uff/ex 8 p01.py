
num = int(input())
cond =input()
contador = 0

while cond == 's' :
    for i in range(1,num ) :
            if num % i == 0 and i != 1 :
                print(i)
                contador += 1

    if contador <  1 :
        print('O número é primo.')
    contador = 0
    num = int(input())
    cond = input()

for i in range(1,num ) :
        if num % i == 0 and i != 1 :
            print(i)
            contador += 1
if contador < 1 :
    print('O número é primo.')









