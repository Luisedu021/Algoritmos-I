from time import sleep
n=int(input('Digite a distância em Km de sua viagem:'))
print('Voce está prestes a começar uma viagem de {} km'.format(n))
vl=n*0.50
vc=n*0.45
print('PROCESSANDO...')
sleep(2)
if n<=200:
    print('Sua viagem custará R${:.2f}'.format(vl))
else:
    print('Sua viagem custará R${:.2f}'.format(vc))
