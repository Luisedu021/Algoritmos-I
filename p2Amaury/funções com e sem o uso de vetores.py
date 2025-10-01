# Problema 1: Pode ser usado sem o uso de vetores
def soma_media(n):
    soma = 0
    for i in range(0,n):
        variavel = int(input('Insira um valor: '))
        soma += variavel
    media = soma / n

    return media

# Problema 2: Deve ser usada com o uso de vetores

def notas_mais_frequentes(n):
    lista_notas = []
    for i in range(0,n):

        nota = float(input())
        lista_notas.append(nota)
    notas_unicas = []
    frequencias = []
    maiores_freq = []

    for nota in lista_notas:
        if nota not in notas_unicas:
            notas_unicas.append(nota)

    for nota in notas_unicas:
        frequencias.append(lista_notas.count(nota))

    maximo = max(frequencias)
    for freq in range(len(frequencias)):
        if frequencias[freq] == maximo:
            maiores_freq.append(int(notas_unicas[freq]))


    return notas_unicas, frequencias,maiores_freq


# Problema 3: Altura e sexo (com/sem vetor)
def analise_alturas_sexo(n):

    soma_alturas_f = 0
    cont_masculinos = 0
    cont_femininos = 0
    altura_max = 0
    altura_min = 0
    for i in range(0,n):

        sexo = input()
        altura = float(input())
        if i == 0:
            altura_max = altura
            altura_min = altura
        if i != 0:
            if altura > altura_max:
                altura_max = altura
            if altura < altura_min:
                altura_min = altura

        if sexo == 'F':
            soma_alturas_f += altura
            cont_femininos += 1
        if sexo == 'M':
            cont_masculinos += 1

    if cont_femininos > 0:
        media = soma_alturas_f / cont_femininos
    else:
        media = 0

    return f'numero de homens: {cont_masculinos},altura máximo: {altura_max},altura mínima: {altura_min},media: {media:.2f}'


# Problema 4: É necessário o uso de vetores

def pesos_acima_abaixo_media(n):
    lista_pesos = []
    soma = 0
    pesos_acima = 0
    pesos_abaixo = 0

    for i in range(0,n):
        peso = float(input())
        lista_pesos.append(peso)
        soma += peso
    media = soma / n

    for peso in lista_pesos:
        if peso > media:
            pesos_acima += 1
        elif peso < media:
            pesos_abaixo += 1

    return pesos_acima,pesos_abaixo

# Problema 5: Pode ser feita sem vetor

def temp_min_max():
    temp_min = 0
    temp_max = 0

    for i in range(0,30):
        temp = float(input())
        if i == 0:
            temp_min = temp
            temp_max = temp
        if temp < temp_min:
            temp_min = temp
        if temp > temp_max:
            temp_max = temp
    return temp_min,temp_max