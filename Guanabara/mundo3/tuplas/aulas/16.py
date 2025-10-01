lanche =( 'hamburger','suco','refrigerante' ,'suco','pudim')
geladeira = 'maça','pera','suco','refrigerante'

#tuplas sao imutaveis

for item in lanche:
    print(item,end = ' ')
print()
print(lanche[-2:])

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')