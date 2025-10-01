md=float(input('Digite um valor em dias:'))
#atribuindo variável de horas
h=24*md
#transformando dias em trídios
t=md/3
#transformando semanas em horas
s=7*h
#transformando semanas em novenas
n= s + 2*md
#transformando em segundos
s1=3600 *h
print('Seu valor resulta em {} horas,  {} segundos e  {} trídios'.format(h,s1,t))

