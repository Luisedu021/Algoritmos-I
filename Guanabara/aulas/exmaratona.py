N = int(input())
estados = list(map(int, input().split(" ")))
rotulos = list(input())

letraAnterior = ""
letraAtual = ""
for i in range(len(rotulos)):
    if i < len(rotulos)-1:
        LetrasAnterior = rotulos[i]
        LetrasAtual = rotulos[i + 1]
        if letraAnterior != LetrasAtual:
            print(f'{LetrasAnterior} -> {LetrasAtual}')
            print('Divide ')
        elif letraAnterior == LetrasAtual:
            print(f'{LetrasAnterior} -> {LetrasAtual}')
            print('Nao Divide')