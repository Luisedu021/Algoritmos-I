# Entrada do usuário
N = int(input())
# Impressão do valor lido
print(N)
# Cálculo das notas
n100 = N // 100
resto = N % 100
n50 = resto // 50
resto %= 50
n20 = resto // 20
resto %= 20
n10 = resto // 10
resto %= 10
n5 = resto // 5
resto %= 5
n2 = resto // 2
n1 = resto % 2
# Impressão no formato correto
print(f"{n100} nota(s) de R$ 100,00")
print(f"{n50} nota(s) de R$ 50,00")
print(f"{n20} nota(s) de R$ 20,00")
print(f"{n10} nota(s) de R$ 10,00")
print(f"{n5} nota(s) de R$ 5,00")
print(f"{n2} nota(s) de R$ 2,00")
print(f"{n1} nota(s) de R$ 1,00")
