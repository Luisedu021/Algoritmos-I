lista = ('lapis',1.75,'Borracha',2,'caderno',15.9,'estojo',25,'transferidor',4.2,'compasso',9.99,'mochila',120.32,'canetas',22.3,'livro',34.9)
print('-'*40)
print('LISTAGEM DE PREÇOS'.center(30))
print('-'*40)

for c in range(0,len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}',end = ' ')
    else:
        print(f'R${lista[c]:>7.2f}')

