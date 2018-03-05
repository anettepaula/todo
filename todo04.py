#coding: utf-8
lista = []
num = int(input("Dime un numero: "))
while num != 0:
	num = int(input("Dime un numero: "))
	lista += [num]
	lista.sort()
print "La lista ordenada de menor a mayor es:",lista
