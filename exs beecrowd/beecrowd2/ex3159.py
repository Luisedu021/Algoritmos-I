teclado = {
    'a': '2', 'b': '22', 'c': '222',
    'd': '3', 'e': '33', 'f': '333',
    'g': '4', 'h': '44', 'i': '444',
    'j': '5', 'k': '55', 'l': '555',
    'm': '6', 'n': '66', 'o': '666',
    'p': '7', 'q': '77', 'r': '777', 's': '7777',
    't': '8', 'u': '88', 'v': '888',
    'w': '9', 'x': '99', 'y': '999', 'z': '9999',
    ' ': '0'
}


def tecla_de(caractere):
    for tecla, letras in {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ' '
    }.items():
        if caractere in letras:
            return tecla
    return ''


def converter_mensagem(mensagem):
    resultado = []
    anterior = ''

    for c in mensagem:
        maiuscula = c.isupper()
        letra = c.lower()
        sequencia = teclado[letra]

        if maiuscula:
            resultado.append('#')

        if anterior:
            mesma_tecla = tecla_de(letra) == tecla_de(anterior)
            if mesma_tecla:

                if not (resultado and resultado[-1] == '#'):
                    resultado.append('*')

        resultado.append(sequencia)
        anterior = letra

    return ''.join(resultado)



n = int(input())
for _ in range(n):
    frase = input()
    print(converter_mensagem(frase))