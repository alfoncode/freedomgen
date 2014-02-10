import os
# -*- coding: utf-8 -*-

extension=".com"

letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


contadorCombinaciones=0;
contadorLibres=0;

archivoResultado = open("resultado.txt","wr")

for r1 in range(0,len(letras)):
	for r2 in range(0,len(letras)):
		for r3 in range(0,len(letras)):
			for r4 in range(0,len(letras)):
				for r5 in range(0,len(letras)):
					
					nombre = letras[r1] + letras[r2] + letras[r3] + letras[r4] + letras[r5]				
					contadorCombinaciones = contadorCombinaciones + 1;

					os.system("whois " + nombre + extension + "> salida.txt")

					archivoSalida = open("salida.txt","r")

					cadenaArchivo=archivoSalida.read()

					archivoSalida.close()

					os.system("rm salida.txt")

					if (cadenaArchivo.find("No match for \"" + nombre.upper() + extension.upper() + "\".") != -1):
						print (nombre + extension + " Libre")
						archivoResultado.write(nombre + extension + " Libre\n")
						contadorLibres = contadorLibres + 1;




print ("Número de combinaciones: " + str(contadorCombinaciones))
archivoResultado.write("Número de combinaciones: " + str(contadorCombinaciones) + "\n")

print ("Número de dominios libres: " + str(contadorLibres))
archivoResultado.write("Número de dominios libres: " + str(contadorLibres) + "\n")

archivoResultado.close()
