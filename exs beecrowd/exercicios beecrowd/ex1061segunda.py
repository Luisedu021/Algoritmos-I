#entrada do usuário
diainicio = input()
inicio = input()
diafim = input()
fim = input()

#formatação para pegar o dia que começa
diainicio = diainicio.split()

diainicio = int(diainicio[1])

 #organizando as horas,minutos e segundos que começa o evento
inicio = inicio.split()

iniciohora = int(inicio [0])
iniciominuto = int(inicio[2])
iniciosegundo = int(inicio [4])

#formatando para pegar o dia que termina
diafim = diafim.split()

diafim = int(diafim[1])

#organizando o fim em horas,minutos e segundos
fim = fim.split()

fimhora = int(fim[0])
fimminuto = int(fim[2])
fimsegundo = int(fim[4])

#convertendo tudo pra segundos
diainicios = diainicio * 24 * 3600
iniciohoras = iniciohora * 3600
iniciominutos = iniciominuto * 60

#convertendo tudo pra segundos
diafims = diafim * 24 * 3600
fimhoras = fimhora * 3600
fimminutos = fimminuto * 60

#somando tudo o inicio
totalinicios =  diainicios + iniciohoras + iniciominutos + iniciosegundo

#somando tudo o final
totalfims = diafims + fimhoras + fimminutos + fimsegundo

#fazendo a diferenca entre os segundos
diferenca = totalfims - totalinicios

#fazemos a divisão inteira para saber os dias,horas,minutos e segundos
dias = diferenca // 86400

resto = diferenca % 86400

horas = resto // 3600

resto %= 3600

minutos = resto // 60

resto %= 60

segundos = resto
#saída desejada
print(dias, 'dia(s)')
print(horas, 'hora(s)')
print(minutos, 'minuto(s)')
print(segundos, 'segundo(s)')




