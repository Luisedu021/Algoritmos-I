from datetime import date
ano = int(input('Ano de nascimento:'))
anoatual = date.today().year
idade = anoatual - ano
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade  <=14 :
    print('INFANTIL')
elif idade <= 19 :
    print('JÚNIOR')
elif idade <= 25 :
    print('SÊNIOR')
elif idade >  25 :
    print('MASTER')
