brasileirao_times = (
    "Flamengo", "Cruzeiro", "Red Bull Bragantino", "Palmeiras", "Fluminense",
    "Botafogo", "Bahia", "Mirassol", "Atlético-MG", "Ceará",
    "Corinthians", "Grêmio", "São Paulo", "Internacional", "Vasco",
    "Vitória", "Fortaleza", "Santos", "Juventude", "Sport"
)

print('-=' * 20)
print(f'Lista dos primeiros 5 colocados  do Brasileirão: {brasileirao_times[0:5]}')
print('-=' * 20)
print(f'Os 4 últimos são: {brasileirao_times[-4:]}')
lista_ordenada = sorted(brasileirao_times)
print('-=' * 20)
print(f'Lista ordenada: {lista_ordenada}')
print('-=' * 20)
print(f'o Corinthians está na posição {brasileirao_times.index('Corinthians') + 1} º')
for j in range(0, len(brasileirao_times)):
    if brasileirao_times[j] == 'Corinthians':
        print(f'o Corinthians está na posição {j + 1} º')
        print('-=' * 20)