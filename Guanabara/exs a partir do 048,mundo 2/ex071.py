
valor = int(input('Qual valor você quer sacar?'))
cedula50 = valor // 50
resto50 = valor % 50
cedula10 = resto50 // 10
resto10 = resto50 % 10
cedula1 = resto10
print(cedula50)
print(cedula10)
print(cedula1)