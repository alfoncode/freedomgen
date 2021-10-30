# -*- coding: utf-8 -*-
import os
import time
from subprocess import PIPE, run

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout					

letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
vocales = ["a","e","i","o","u"]
consonantes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
custom = ["n","y","x"]

for r1 in range(0,len(vocales)):
	for r2 in range(0,len(consonantes)):
		for r3 in range(0,len(vocales)):
			for r4 in range(0,len(custom)):								
				nombre = vocales[r1] + consonantes[r2] + vocales[r3] + custom[r4]											
				output = out("whois " + nombre + ".com|grep \"No match for domain\"" + ">> salida.txt")					


