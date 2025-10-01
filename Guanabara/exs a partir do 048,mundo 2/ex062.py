print('Gerador de PA')
print('-='*20)
n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
qtd = 10
contador = 0
while qtd > 0:
    print(n1,end = ' -> ')
    n1 += r
    qtd -= 1
    if qtd == 0:
        print('PAUSA')
        qtd = int(input('Quantos termos voce quer mostrar a mais?'))
    contador += 1

print('Progressão finalizada com {} termos mostrados'.format(contador))