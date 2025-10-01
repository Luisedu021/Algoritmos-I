import math as m1
print('Relações trigonométricas')
ang=(input('Digite um angulo em radianos:'))
ang1=float (ang)
ang2 = m1.radians(ang1)
seno=m1.sin(ang2)
cos=m1.cos(ang2)
tan=m1.tan(ang2)
print('O cosseno,seno,tangente de {}º são respectivamente: {:.2f} ; {:.2f} e {:.2f}'.format(ang1,cos,seno,tan))





