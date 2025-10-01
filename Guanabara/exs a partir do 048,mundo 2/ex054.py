from datetime import date
atual = date.today().year

contador_menor = 0
contador_maior = 0

for i in range(0,7):
    ano = int(input('Em que ano a {} ª pessoa nasceu?'.format(i + 1)))
    if atual - ano <= 18 :
        contador_menor  += 1
    else:
        contador_maior += 1

if contador_menor > 1 :
    print('Ao todo tivemos {} pessoas menores de idade'.format(contador_menor))
    if contador_maior > 1:
        print('Ao todo tivemos {} pessoas maiores de idade'.format(contador_maior))

    else:
        print('Ao todo tivemos {} pessoa maior  de idade'.format(contador_maior))

elif contador_menor <= 1 :
    print('Ao todo tivemos {} pessoa menor de idade'.format(contador_menor))
    if contador_maior > 1:
        print('Ao todo tivemos {} pessoas maiores de idade'.format(contador_maior))

    else:
        print('Ao todo tivemos {} pessoa maior  de idade'.format(contador_maior))

