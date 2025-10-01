comparador = 0

n = int(input())
parametro = 10000000
for i in range(1,n+ 1):
    m = int(input())
    if m < parametro:
        parametro = m
        dia = i

print(f'Foram coletados {parametro} mosquitos no dia {dia}')