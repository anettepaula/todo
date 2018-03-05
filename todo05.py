#coding: utf-8
lista = []
num = int(input("Dime un numero: "))
while num != 0:
	num = int(input("Dime un numero: "))
	lista += [num]
	lista.sort()
	lista.reverse()
print "La lista ordenada de mayor a menor es:",lista
