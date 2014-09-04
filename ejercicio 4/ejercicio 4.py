def valor_cadena(cad_1,cad_2):
	if len(cad_1)>len(cad_2):
		print cad_1
	if len(cad_2)>len(cad_1):
		print cad_2
	if len(cad_1)==len(cad_2):
		print cad_1+cad_2
	
cad_1=raw_input("ingrese la cadena1:")
cad_2=raw_input("ingrese la cadena2:")
valor_cadena(cad_1,cad_2)