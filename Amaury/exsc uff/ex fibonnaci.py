
fib = 0
f1 = 0
f2 = 1

n = int(input())
if n == 0:
    print(0)
elif n == 1:
    print('0, 1')

else:
    for i in range(0,n + 1):
        fib = fib + f1
        f1 = f2
        f2 = fib
        if i == n :
            print(fib)
        else:

            print(str(fib) + ',' , end=' ' )

