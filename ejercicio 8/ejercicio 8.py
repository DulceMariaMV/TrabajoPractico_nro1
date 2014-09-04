def triangulo(l1,l2,l3):
	if teorema_pitagoras(l1,l2,l3):
		return "Rectangulo"
	if l1==l2 and l2==l3:
		return "Equilatero"
	if l1==l2 and l2!=l3:
		return "Isoseles"
	if l1!=l2 and l2==l3:
		return "Isoseles"
	if l1==l3 and l3!=l2:
		return "Isoseles"
	if l1!=l2 and l2!=l3:
		return "Escaleno"
	return "No es triangulo"
  
def teorema_pitagoras(a,b,c):
	cate=0
	hipo=0
	may=0
	if a>b and a>c:
		hipo=a*a
		cate=(c*c)+(b*b)
	if b>a and b>c:
		hipo=b*b
		cate=(a*a)+(c*c)
	if c>a and c>b:
		hipo=c*c
		cate=(a*a)+(b*b)
	if hipo==cate:
		return True
	else:
		return False


lado1=int(raw_input("ingrese el lado1:"))
lado2=int(raw_input("ingrese el lado2:"))
lado3=int(raw_input("ingrese el lado3:"))
print triangulo(lado1,lado2,lado3)