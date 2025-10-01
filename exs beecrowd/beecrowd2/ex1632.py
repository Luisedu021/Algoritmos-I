n = int(input())

for i in range(n):
    total = 1

    frase = input()
    for j in range(len(frase)):

        comparador = frase[j].lower()
        if comparador == 'a' or comparador == 'e' or comparador == 'i' or comparador == 'o' or comparador == 's' :
            total  *= 3
        else:
            total *= 2
    print(total)

