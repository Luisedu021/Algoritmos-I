nome=str(input('Digite uma frase:'))
nome.lower()
nf= nome.strip()
f = nf.count('a')
if f <= 1 : print('Seu nome possui {} letra a '.format(f))
else : print('Seu nome possui {} letras a'.format(f))
pv= nome.find('a')
print('A letra a aparece pela primeira vez no espaço: {}'.format(pv))
uv=nome.rfind('a')
print('A letra a aparece pela ultima vez na posição: {}'.format(uv))










