#coding: utf-8

meses = ("Error","enero","febrero","marzo","abril","marzo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")

num = int(input("Dime un número: "))
if num == 0:
    print "Error."

while num>12 :
	num = int(input("Error. Dime otro número: "))

else :
	print meses[num]	
