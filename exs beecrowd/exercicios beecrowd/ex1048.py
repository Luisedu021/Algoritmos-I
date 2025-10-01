salario = float(input())
s15 = (salario*115/100)
s12 = (salario*112/100)
s10 = (salario*110/100)
s07 = (salario*107/100)
s04 = (salario*104/100)
r15 =(salario*15/100)
r12 = (salario*12/100)
r10 = (salario*10/100)
r07 =(salario*7/100)
r04 = (salario*4/100)
if salario<=400:
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {}'.format(round(s15,2),round(r15,2),'15 %'))
elif 400 <salario <=800:
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {}'.format(round(s12),round(r12),'12 %'))
elif 800 <salario <=1200:
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {}'.format(round(s10,2),round(r10,2),'10 %'))
elif 1200 < salario <=2000 :
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {}'.format(round(s07,2),round(r07,2),'7 %'))
else :
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {}'.format(round(s04,2),round(r04,2),'4 %'))