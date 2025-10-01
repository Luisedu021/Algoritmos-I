total = 151
n = int(input())
Lista= []


for pokemon in range(0,n):
    Lista.append(input())

Lista_sem_rep = set(Lista)
Lista_sem_rep = list(Lista_sem_rep)
n1 = len(Lista_sem_rep)

print(f'Falta(m) {total - n1} pomekon(s).')