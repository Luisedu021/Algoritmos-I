data = []
while True:
    try:
        n,d = map(int,input().split())
        for i in range(d):
            datas = input().split()

            presenca = datas[1:]
            if '0' not in presenca:
                data.append(datas[:1])

        if len(data) != 0:
            print(data[0][0])
        else:
            print('Pizza antes de FdI')
        data = []

    except EOFError:
        break



