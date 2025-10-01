tentativas = int(input())
for j in range(tentativas):
        n = int(input())
        soma = 0
        for i in range(1,n):
            if n % i == 0:
                soma += i
        if soma == n:
            print(f'{n} eh perfeito')
        else:
            print(f'{n} nao eh perfeito')
            