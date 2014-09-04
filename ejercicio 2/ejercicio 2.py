
	

def function(inicio,fin):	
	inicio 
	fin 
	lista=[]
	lista2=[]
	for x in xrange(inicio,fin+1):
		lista.append(x)
	print lista
	for x in lista:
		if x%2==0:
			lista2.append(x)
	print lista2

inicio = int(raw_input("ingrese el inicio:"))
fin = int(raw_input("ingrese el final:"))
function(inicio,fin)