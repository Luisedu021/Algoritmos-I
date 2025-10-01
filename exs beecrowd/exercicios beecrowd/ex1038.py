#entrada do usuário
c,qtd = map(int,input().split())
#colocando variáveis caso eu queira mudar o preço posteriormente e para mecher no float number deles conforme o exercicio pediu
cq = qtd *4
xsalada = qtd *4.50
xbacon = qtd*5.00
t= qtd *2
r= qtd*1.50
#adicionando as condicionais conforme o preço pedido,nesse caso se o codigo for 1,teremos cachorro quente que vale 4 reais cada um
if c == 1:
    print(f'Total: R$ {cq:.2f}')
elif c == 2:
    print(f'Total: R$ {xsalada:.2f}')
elif c == 3 :
    print(f'Total: R$ {xbacon:.2f}' )
elif c == 4 :
    print(f'Total: R$ {t:.2f}')
elif c ==5 :
    print(f'Total: R$ {r:.2f}')


