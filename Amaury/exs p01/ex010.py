from math import pi

raio = float(input('Digite o valo do raio: '))

perimetro = 2 * pi * raio
area = pi * raio ** 2
print('O perímetro vai ser de {:.3f} unidades e a área vai ser de {:.3f} unidades ao quadrado.'.format(perimetro, area))
