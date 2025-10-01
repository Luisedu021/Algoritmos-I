from datetime import date
ano = int(input('Qual ano voce nasceu?'))
genero = input('Qual o seu gênero?')
anoatual = date.today().year
idade = anoatual - ano
print('Voce possui {} anos'.format(idade))
genero = genero.lower().strip()
if genero == 'masculino' or genero == ' homem' :
    if idade < 18:
         print('Você nao precisa se alistar')
    elif idade == 18:
        print('Está na hora de se alistar')
    elif idade > 18:
        print('Já passou da hora de se alistar')
else :
    print('Voce não é obrigada a se alistar')