print('Aluguel de carros')
#aplicando variáveis
d=float(input('Quantos dias alugados? '))
km:float=float(input('Quantos Km rodados?'))
vd=60
vkm=0.15
vt= (vd*d) + (vkm*km)
print('O Valor do km rodado é de {} reais e o valor do dia é de {} reais'.format(vd,vkm))
print('Portanto voce andará {}'.format(vt))

