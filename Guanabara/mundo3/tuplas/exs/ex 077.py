palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')

for p in range(len(palavras)):
    vogais_usadas = ''
    ord = ''
    for caracter in palavras[p]:

        if caracter == vogais[0]:
            vogais_usadas =  vogais_usadas + caracter
        if caracter == vogais[1]:
            vogais_usadas =  vogais_usadas + caracter
        if caracter == vogais[2]:
            vogais_usadas =  vogais_usadas + caracter
        if caracter == vogais[3]:
            vogais_usadas =  vogais_usadas + caracter
        if caracter == vogais[4]:
            vogais_usadas =  vogais_usadas + caracter
    for vogal in vogais_usadas:

        ord += ' ' + vogal
    print(f'Na palavra {palavras[p]} temos {ord}')
