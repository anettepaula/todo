#coding: utf-8
listaPalabras = []
palabras = []
num = int(input("Dime cuantas palabras tiene la lista: "))
for i in range(num):
	pal = raw_input("Dime la palabra: ")
	listaPalabras += [pal]

prefijo = raw_input("Dime un prefijo: ")
def inicianCon(listaPalabras, prefijo):
	for i in(listaPalabras):
		if (i.find(prefijo,0,len(prefijo))>=0):		
			palabras.append(i)
inicianCon(listaPalabras, prefijo)
	
print "Las palabras que comienzan con",prefijo,"son:",palabras

print (inicianCon(listaPalabras, prefijo))
	
