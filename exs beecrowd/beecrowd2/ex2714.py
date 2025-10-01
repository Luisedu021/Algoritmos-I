n = int(input())
for _ in range(n):
    senha = input().strip()

    if len(senha) != 20 or not senha.startswith("RA") or not senha[2:].isdigit():
        print("INVALID DATA")
    else:
        num = senha[2:].lstrip("0")
        if num:
            print(num)
        else:
            print("0")