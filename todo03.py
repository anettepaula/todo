#coding: utf-8
num = int(input("Dime un numero: "))
tabla = []
por = 10
for i in range(por):
	multi = (i+1)*num
	tabla += [multi]
print "La lista de multiplicar es:",tabla
	
