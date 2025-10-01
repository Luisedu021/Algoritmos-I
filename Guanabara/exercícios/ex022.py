'''print('Leitor de nomes')
#ATRIBUINDO VARIÁVEIS
nome = (str)(input('Digite o seu nome completo:'))
n1=nome.upper()
n2=nome.lower()
#DIVIDINDO AS STRINGS
ns=nome.split()
#JUNTANDO SEM OS ESPAÇOS
nj=''.join(ns)
#CONTANDO OS CAR.
cnj=len(nj)
#ATRIBUINDO O PRIMEIRO NOME/CONTANDO
Pn=ns[0]
cpn=len(Pn)
print('O seu nome em letras maiúsculas fica: {}.'.format(n1))
print('O seu nome em letras minúsculas fica: {}'.format(n2))
print('Seu primeiro nome possui {} letras'.format(cpn))
print('Seu Nome completo possui {} letras'.format(cnj))'''
nome = str(input('Digite seu nome completo: ')) . strip()
print ('Analisando seu nome...')
print('Seu nome em minúsculas fica:{}'.format(nome.lower()))
print('Seu nome em maiúsculas fica: {}'.format(nome.upper()))
print('Seu nome possui {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome possui {} letras'.format(len(nome.split()[0])))














