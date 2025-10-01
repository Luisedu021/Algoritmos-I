#importar a biblioteca do sorteador e do recurso visual do jokenpo
from random import choice
from time import sleep

#adicionando cores para deixar a interface mais bonita
cores = {'limpa': '\033[m',
         'verde' : '\033[1;32m',
        'vermelho': '\033[1;31m' }

#interface inicial do jogo
print('{}JOGO PEDRA, PAPEL E TESOURA{}'.format(cores['verde'],cores['limpa']))
ver = ''
while ver != 'N':
    #entrada do usuário
    jogada = input('Digite Pedra,papel ou tesoura:')

    #formatação da entrada para as condicionais
    jogada = jogada.upper().strip()

    #adicionando a lista de opções de escolha do pc
    lista = ['PEDRA','PAPEL','TESOURA']

    #sorteador da lista
    jogadapc = choice(lista)

    #adicionando um recurso visual de time
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    print(' ')
    #condicional de caso ambas as jogadas sejam iguais
    if jogada == jogadapc:
        print('Você escolheu {} e o computador escolheu {}! {} Ninguém ganhou:({}'.format(
                                                                                                jogada,jogadapc,cores['vermelho'],cores['limpa']))

    #aninhando condicionais caso a primeira jogada seja de pedra e indentando as possibilidades

    elif jogada == 'PEDRA':
            if jogadapc == 'PAPEL' :
                      print('Voce jogou {} e o pc jogou {}, logo, {}você perdeu !{}'.format(jogada,jogadapc,cores['vermelho'],cores['limpa']))
            else:
                     print('Voce jogou {} e o pc jogou {}, logo, {}você ganhou !{}'.format(jogada,jogadapc,cores['verde'],cores['limpa']))

    #aninhando condicionais caso a primeira jogada seja de pedra e indentando as possibilidades

    elif jogada == 'PAPEL':

            if jogadapc == 'TESOURA':
                    print('Voce jogou {} e o pc jogou {}, logo, {}você perdeu !{}'.format( jogada, jogadapc,cores['vermelho'] , cores['limpa']))
            else :
                    print('Voce jogou {} e o pc jogou {}, logo, {}você ganhou !{}'.format(jogada,jogadapc,cores['verde'], cores['limpa']))

    #aninhando condicionais caso a primeira jogada seja de pedra e indentando as possibilidades

    elif jogada == 'TESOURA':

                if jogadapc == 'PEDRA':
                        print('Voce jogou {} e o pc jogou {}, logo, {}você perdeu !{}'.format( jogada,jogadapc, cores['vermelho'], cores['limpa']))
                else :
                        print('Voce jogou {} e o pc jogou {}, logo, {}você ganhou !{}'.format( jogada,jogadapc, cores['verde'], cores['limpa']))

    #adicionando uma opção caso a entrada seja != de pedra,papel ou tesoura

    else:
                print('{}ENTRADA INVÁLIDA!\033[m'.format(cores['vermelho']))
    print(' ')
    ver = input('Quer jogar novamente? [S/N] : ').upper()[0]

print('{}Fim de jogo!\033[m'.format(cores['vermelho']))




