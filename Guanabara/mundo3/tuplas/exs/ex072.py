numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
           'onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o numero {numeros[n]}')
        ver = input('Voce quer continuar?[S/N]')
        if ver[0].upper() == 'N':
            break
    print('Tente novamente!', end=' ')

