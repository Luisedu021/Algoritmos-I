#entrada do usuário
renda = float(input())
#adicionando variáveis e o resto para fazer a porcentagem
taxa1 = ( 1000)*8/100
v1 = (renda -2000)*8/100
taxa2 = (renda - 3000)*18/100
taxa3 = (renda - 4500)*28/100
v2 = taxa1 + taxa2
v3 = taxa1 + (1500*18/100) + taxa3
#adicionando condicionais
if renda <= 2000:
    print('Isento')
elif 2000 < renda <= 3000:
   print('R$ {:.2f}'.format(v1))
elif 3000 < renda <= 4500:
    print('R$ {:.2f}'.format(v2))
elif  renda > 4500:
    print('R$ {:.2f}'.format(v3))
