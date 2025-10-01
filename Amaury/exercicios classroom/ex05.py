moeda = int(input('Digite o valor total de centavos'))
um_real = moeda //100
resto = moeda % 100
cinqnt = resto // 50
resto %= 50
vinte_cinco = resto // 25
resto %=25
dez = resto // 10
resto %= 10
cinco = resto //5
resto %= 5
um = resto
print('{} moedas de 1 real\n{} moedas de 50 centavos\n{} moedas de 25\n{} '
      'moedas de 10\n{} moedas de 5\n{} moedas de 1 centavos'.format(um_real,cinqnt,vinte_cinco,dez,cinco,um))
