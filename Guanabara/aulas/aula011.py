a = 3
b= 5
print('Os valores são \033[1;36m{}\033[m e \033[1;36m{}\033[m'.format(a,b))
nome ='Luis'
print('0lá!Muito prazer em te conhecer,{}{};){}'.format('\033[1;34m',nome,'\033[1;36m'))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}
print('{}Olha,que legal{}\033[m'.format(cores['pretoebranco'],cores['pretoebranco']))



