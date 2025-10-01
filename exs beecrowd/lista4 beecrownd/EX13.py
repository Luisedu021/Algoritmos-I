n = int(input())

velocidades = input().split()
poscerta = 0

for pos,velocidade  in enumerate(velocidades):

    if pos == 0:
        velocidade0 = int(velocidade)
    else:
            if  int(velocidade) < velocidade0:
                poscerta = pos + 1
                break
            else:
                velocidade0 = int(velocidade)

print(poscerta)
