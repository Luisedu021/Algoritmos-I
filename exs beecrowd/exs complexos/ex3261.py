import sys

# Loop para ler cada linha da entrada padrão (stdin)
for line in sys.stdin:
    line = line.strip()  # Remove caracteres de nova linha do final da string

    # Se a linha for vazia (após remover espaços em branco), imprime uma nova linha e continua para a próxima entrada
    if not line:
        print()
        continue

    # Conjunto para armazenar letras únicas e garantir a ordem alfabética ao converter para lista e ordenar
    letras_validas = set()
    for char in line:
        # Verifica se o caractere é uma letra minúscula de 'a' a 'z'
        if 'a' <= char <= 'z':
            letras_validas.add(char)

    # Se não houver letras válidas na linha (ex: linha com apenas espaços ou caracteres especiais),
    # imprime uma nova linha e continua
    if not letras_validas:
        print()
        continue

    # Converte o conjunto de letras para uma lista e a ordena alfabeticamente
    letras_ordenadas = sorted(list(letras_validas))

    faixas = []

    # Inicializa a primeira faixa com a primeira letra ordenada
    start_range = letras_ordenadas[0]
    end_range = letras_ordenadas[0]

    # Itera pelas letras ordenadas a partir da segunda letra
    for i in range(1, len(letras_ordenadas)):
        current_char = letras_ordenadas[i]

        # Verifica se a letra atual é a próxima consecutiva da faixa
        if ord(current_char) == ord(end_range) + 1:
            end_range = current_char  # Estende a faixa atual
        else:
            # Se não for consecutiva, a faixa anterior terminou. Adiciona-a à lista de faixas.
            if start_range == end_range:
                faixas.append(f"{start_range}:{start_range}")
            else:
                faixas.append(f"{start_range}:{end_range}")

            # Inicia uma nova faixa com a letra atual
            start_range = current_char
            end_range = current_char

    # Após o loop, adiciona a última faixa processada
    if start_range == end_range:
        faixas.append(f"{start_range}:{start_range}")
    else:
        faixas.append(f"{start_range}:{end_range}")

    # Imprime as faixas separadas por ", "
    print(", ".join(faixas))