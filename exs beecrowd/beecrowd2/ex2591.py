n = int(input())

while n > 0 :
    n -= 1
    frase = input()
    frase = frase.split('k')
    ka =  'k' + frase[0].count('a') * frase[1].count('a') * 'a'
    print(ka)
