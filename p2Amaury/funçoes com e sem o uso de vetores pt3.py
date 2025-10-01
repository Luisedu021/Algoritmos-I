# Problema 8: Deve usar vetores
def mediana_idades(n):
    valores = []
    for i in range(n):
        idade = int(input())
        valores.append(idade)
    valores.sort()
    if n % 2 == 0:
        mediana = (valores[len(valores)//2] + valores[len(valores)//2 - 1]) / 2
    else:
        mediana = valores[len(valores)//2]
    return mediana

# Problema 9: Boi mais gordo e mais magro (pode ser feito sem o uso de vetores)
def boi_gordo_magro(n):
    pboi_gordo = 0
    pboi_magro = 0
    boi_gordo = 0
    boi_magro = 0

    for i in range(n):
        peso = int(input())
        codigo = input()

        if i == 0:
            boi_gordo  = codigo
            pboi_gordo = peso
            boi_magro = codigo
            pboi_magro = peso
        else:
            if peso > pboi_gordo:
                pboi_gordo = peso
                boi_gordo = codigo
            elif peso < pboi_magro:
                pboi_magro = peso
                boi_magro = codigo

    return pboi_gordo, boi_gordo,pboi_magro, boi_magro


# Problema 10: Concurso de belezas - maiores alturas e quantidade (com/sem vetor)
def concurso_belezas(n):
    maior1 = 0
    maior2 = 0
    cont1 = 0
    cont2 = 0

    for i in range(n):
        altura = float(input())
        cod = input()

        if altura > maior1:
            # A nova altura vira a primeira maior
            maior2 = maior1
            cont2 = cont1
            maior1 = altura
            cont1 = 1
        elif altura == maior1:
            cont1 += 1
        elif altura > maior2:
            maior2 = altura
            cont2 = 1
        elif altura == maior2:
            cont2 += 1

    return f"A maior altura é {maior1} e aparece {cont1} vez(es)",f"A segunda maior altura é {maior2} e aparece {cont2} vez(es)"

print(concurso_belezas(3))