#entrada do usuário com as notas
N1,N2,N3,N4 = map(float,input().split())
#aplicando a media conforme pedido no exercício
media = (N1*2 + N2*3 + N3*4 + N4)/10
#aplicando as condições caso a media seja maior que 7
if media >= 7 :
    print('Media: {:.1f}'.format(media))
    print('Aluno aprovado.')
#aplicando caso a media seja inferior a 5
elif media < 5:
    print('Media: {:.1f}'.format(media))
    print('Aluno reprovado.')
#aplicando a condiconal e recalculando a media caso a media esteja entre 5 e 7(não conta o 7)
elif  5<=media <=6.9:
    exame = float(input())
    medianova = (exame + media) / 2
    print('Media: {:.1f}'.format(media))
    print('Aluno em exame.')
    print('Nota do exame: {:.1f}'.format(exame))
    if medianova >=5.0 :
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(medianova))
    else :
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(medianova))