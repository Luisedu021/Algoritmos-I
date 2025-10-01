from random import randint
from time import sleep

jogadores =dict()
jogadores_ordem = list()

jogadores['jogador1'] = randint(1,6)
jogadores['jogador2'] = randint(1,6)
jogadores['jogador3'] = randint(1,6)
jogadores['jogador4'] = randint(1,6)

for k, v in jogadores.items():
    print(f'O {k} tirou {v} ')
    print(jogadores.get(v))
    sleep(1)

print(jogadores)