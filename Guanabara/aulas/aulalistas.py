'''teste = list()
teste.append('Luis')
teste.append(19)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)'''

galera = list()
dado = []
for c in range(0,2):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()


for p in galera:
    print(f'Pessoas: {p[0].capitalize()} , Idade: {p[1]}')