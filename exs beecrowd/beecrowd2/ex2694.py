n = int(input())

for j in range(n):
    frase = input()
    primeiro_termo = int(frase[2:4])
    segundo_termo = int(frase[5:8])
    terceiro_termo = int(frase[11:13])
    soma = primeiro_termo + segundo_termo + terceiro_termo
    print(soma)