def es_palindromo(cadena):
	if str(cadena[::-1])==cadena:
		print("True")
		print("Es una palabra palindromo")
	else:
		print("False")
		print("No es una palabra palindromo")

cadena=raw_input("escriba la palabra:")
es_palindromo(cadena)