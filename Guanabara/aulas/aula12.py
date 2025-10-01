import datetime
nome = str(input('Qual o seu nome?'))
nome1 = nome.lower()
nome1 = nome1.strip()
nome2 = nome.capitalize()
#variavel para pegar hoario do pc
horario = datetime.datetime.today().hour

if nome1 == ('luis') or nome1 == 'luís' or nome1 == 'luiz'  :
    print('Que nome bonito!')
elif nome1 == 'pedro' or nome1 == 'maria' or nome1 =='paulo' :
    print('Seu nome é bem popular no Brasil,mesmo!')
else :
    print('Seu nome é normal!')
if   0 <= horario  < 12 :
    print('Tenha um bom dia, {}!'.format(nome2))
elif 12 <= horario < 18 :
    print('Tenha uma boa tarde, {}!'.format(nome2))
else  :
    print ('Tenha uma boa noite , {}!'.format(nome2))
