print('Conversor de medidas')
n1=float(input('Digite um valor em metros:'))
km=n1/1000
hm=n1/100
dam=n1/10
dm=n1*10
cm=n1*100
mm=n1*1000
print('A medida de {} metros  corresponde a: \n{} km.  \n{}hm \n{}dam  '.format(n1,km,hm,dam))
print('{}dm \n{}cm\n{}mm '.format(dm,cm,mm))

