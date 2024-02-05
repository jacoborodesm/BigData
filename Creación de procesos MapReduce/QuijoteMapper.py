#!/usr/bin/python3
import sys
import re

#Sobre cada línea de entrada, eliminamos los espacios en blanco, encontramos todas las palabras y emitimos un valor de 1 para contar su ocurrencia 

for line in sys.stdin:
    line = line.strip()
    words = re.findall(r'\w+', line.lower())
    for word in words:
        print(f"{word}\t1")
