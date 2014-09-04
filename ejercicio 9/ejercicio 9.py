def primos(n):
	if n==2:
	    return True
	for x in xrange(2,n):
		if n%x==0:
		   return False
	return True


def suma_primos(n):
	x=2
	suma=0
	con=1
	while con<=n:
		if primos(x):
			suma=suma+x
			con=con+1
		x=x+1
	print(suma)

n= int(raw_input("ingrese un numero: "))
suma_primos(n)