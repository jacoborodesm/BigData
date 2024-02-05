#!/usr/bin/python3

import sys

# Definimos las variables de alumno actual y nota máxima 

alumno_actual = None
nota_max = float('-inf')

# Sobre cada linea de entrada la dividimos en alumno y nota y convertimos nota en un entero

for line in sys.stdin:
    alumno, nota = line.split('\t')
    nota = int(nota)

    # Si el alumno es el mismo que el anterior en el bucle actualiza la nota máxima siempre que la clasificación sea mayor
    
    if alumno_actual == alumno:
        nota_max = max(nota_max, nota)
    
    # Si el alumno es diferente al anterior en el bucle siempre que no sea la primera iteración imprimimos el nombre del alumno y su nota máxima
    
    else:
        if alumno_actual:
            print(f'{alumno_actual}\t{nota_max}')
        
        # Reiniciamos los valores de alumno actual y nota max
        
        alumno_actual = alumno
        nota_max = nota

# Para finalizar imprimimos la nota max del último estudiante
        
if alumno_actual:
    print(f'{alumno_actual}\t{nota_max}')
