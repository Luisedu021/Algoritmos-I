nome, nacionalidade = input("Qual o seu nome e nacionalidade?").split()
altura,idade,peso = map(float,input('Qual a sua altura em m , idade e peso?').split())
nacionalidade = nacionalidade.lower().strip()
print('Olá,{}!'.format(nome))
print('Voce é {},tem {} metros, {} anos de idade e pesa {} kg'.format(nacionalidade,altura,idade,peso))




