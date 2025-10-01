idade=int(input())
anos= idade//365
resto=idade%365
meses=resto//30
resto2=resto%30
dias=resto2
print(f'{anos:.0f} ano(s)')
print(f'{meses:.0f} mes(es)')
print(f'{dias:.0f} dia(s)')

