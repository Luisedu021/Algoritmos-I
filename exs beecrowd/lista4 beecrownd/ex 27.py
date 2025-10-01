amigos_antigos = input().split()
amigos_novos = input().split()
amigo_s = input()

lista_nova = []

if amigo_s in amigos_antigos:
    lista_nova += amigos_antigos[:amigos_antigos.index(amigo_s)]
    lista_nova += amigos_novos
    lista_nova += amigos_antigos[amigos_antigos.index(amigo_s):]
else:
    lista_nova += amigos_antigos
    lista_nova += amigos_novos

print(' '.join(lista_nova))