alunos = dict()
alunos['nome'] = str(input('Nome: '))
alunos['média'] = float(input(f'Média de {alunos["nome"]}: '))
print(f'Nome é igual a {alunos["nome"]}.')
print(f'A média é igual {alunos["média"]}')
print('Situação é igual a ',end ='')
if alunos['média'] >= 7:
    print('Aprovado')
else:
    print('Reprovado')