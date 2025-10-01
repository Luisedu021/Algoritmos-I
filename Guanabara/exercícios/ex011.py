l=float(input('Digite a largura da parede em metros:'))
a=float(input('Digite a altura da parede em metros:'))
area=l*a
tinta=area/2
print('Sua parede tem a dimensão {}x{} e sua área é de {} m²'.format(l,a,area))
print('Tendo em vista que a cada 2m² é necessário  um 1 litro de tinta pra ser pintado,voce usará  {} litros de tinta para pintar a parede'.format(tinta))
