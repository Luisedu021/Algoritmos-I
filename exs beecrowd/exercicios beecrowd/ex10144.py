#adicionando variáveis
a, b = map(int, input().split())
#adicionando as condicionais do exercício
if a > b and  a%b == 0  :
    print ('Sao multiplos')
elif a <b and b%a == 0 :
    print('Sao multiplos')
elif a>b and a%b != 0 :
    print('Nao sao multiplos')
elif a<b and b%a != 0 :
    print('Nao sao multiplos')



