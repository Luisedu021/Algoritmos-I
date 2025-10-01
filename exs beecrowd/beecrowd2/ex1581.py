n = int(input())
linguas = []

linguas2= []

for c in range(n):
    qtd = int(input())

    for k in range(qtd):
        linguas.append(input())

    linguas_semrep= set(linguas)
    listanova= list(linguas_semrep)

    if len(linguas_semrep) == 1:
        print(listanova[0])
    else:
        print('ingles')
    linguas = []



