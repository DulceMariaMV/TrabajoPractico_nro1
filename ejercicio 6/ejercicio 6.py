#coding: utf8 
def calcular_letras_numeros(frase):
	letras=0
	digitos=0
	for x in frase:
		if x.isalpha():
			letras=letras+1
		if x.isdigit():
			digitos=digitos+1
	print(str(letras)+" "+str(digitos))

frase=raw_input("escriba una frase")
calcular_letras_numeros(frase)