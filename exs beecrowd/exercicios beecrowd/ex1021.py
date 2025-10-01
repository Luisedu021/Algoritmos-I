# Entrada do usuário
N = float(input())
#Conversão em centavos para evitar problemas
centavos=int(round(N*100))
#Notas
n100=centavos  // 10000
centavos %=10000
n50 = centavos // 5000
centavos %=5000
n20=centavos //2000
centavos %=2000
n10 = centavos //1000
centavos %=1000
n5=centavos // 500
centavos %=500
n2 = centavos //200
#parte das moedas
'''Iremos agora multiplicar por 100 as variáveis e fazer o mesmo raciocínio aplicado la em cima'''
centavos  %= 200
m1= centavos  // 100
centavos %= 100
m50 = centavos//50
centavos %=50
m25 = centavos //25
centavos %=25
m10= centavos //10
centavos %=10
m05=centavos//5
centavos %=5
m01 = centavos
# Impressão no formato correto
print('NOTAS:')
print(f"{n100} nota(s) de R$ 100.00")
print(f"{n50} nota(s) de R$ 50.00")
print(f"{n20} nota(s) de R$ 20.00")
print(f"{n10} nota(s) de R$ 10.00")
print(f"{n5} nota(s) de R$ 5.00")
print(f"{n2} nota(s) de R$ 2.00")
#aplicando as moedas decimas agora'
print('MOEDAS:\n{:.0f} moeda(s) de R$ 1.00\n{:.0f} moeda(s) de R$ 0.50\n{:.0f} moeda(s) de R$ 0.25\n{:.0f} moeda(s) de R$ 0.10\n{:.0f} moeda(s) de R$ 0.05\n{:.0f} moeda(s) de R$ 0.01'.format(m1,m50,m25,m10,m05,m01))



