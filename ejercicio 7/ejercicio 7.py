def generar(n):
	for x in xrange(1,n+1):
		print str(x)*x
	x=n-1
	while x:
		print str(x)*x
		x=x-1
n=int(raw_input("ingrese un numero:"))
generar(n)