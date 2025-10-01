nome=str(input('Digite o nome da sua cidade:'))
nome=nome.split()
lista1=nome[0]
cont=lista1.count('Santo')
if cont==1: print('Sua cidade  possui Santo no  primeiro nome ')
else: print('Sua cidade não possui Santo no primeiro nome')


