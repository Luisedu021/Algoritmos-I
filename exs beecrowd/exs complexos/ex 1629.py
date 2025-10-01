def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))
    print('@')

while True:
    try:
        n = int(input())
        if n == 0:
            break

        mov = n * n

        matrix = [['O' for _ in range(n)] for _ in range(n)]
        x, y = n // 2, n // 2

        direcoes = [(0, 1), (-1, 0), (0, -1), (1, 0)]

        step_size = 1
        mov_cont = 0

        matrix[x][y] = 'X'
        print_matrix(matrix)
        mov -= 1

        while mov> 0:
            for direcao in direcoes:
                for _ in range(step_size):
                    if mov == 0:
                        break

                    x += direcao[0]
                    y += direcao[1]

                    matrix = [['O' for _ in range(n)] for _ in range(n)]
                    matrix[x][y] = 'X'
                    print_matrix(matrix)
                    mov -= 1
                mov_cont += 1

                if mov_cont % 2 == 0:
                    step_size += 1
    except EOFError:
        break