matriz = [
    [1,2],
    [1,2],
    [1,2]
]
matriznova = []
for linha in matriz:
    for coluna in linha:
        nome = input('Digite seu nome:')
        idade = input('Digite sua idade:')
        matriznova.append([nome, idade])

print(matriznova)
