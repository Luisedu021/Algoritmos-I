dia_0 = int(input().split()[1])
horario_0 = input().split(' : ')

horas_0 = int(horario_0[0])
minutos_0 = int(horario_0[1])
segundo_0 = int(horario_0[2])

dia_f = int(input().split()[1])
horario_f = input().split(' : ')

horas_f = int(horario_f[0])
minutos_f = int(horario_f[1])
segundo_f = int(horario_f[2])

diferenca = (dia_f * 24 * 3600 + horas_f *3600 + minutos_f * 60 + segundo_f) - (dia_0 * 24 * 3600 + horas_0*3600 + minutos_0* 60 + segundo_0)

dias = diferenca // (24 * 3600)
resto = diferenca % (24 * 3600)
horas = resto // 3600
resto %= 3600
minutos = resto // 60
resto %= 60
segundos = resto

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')
