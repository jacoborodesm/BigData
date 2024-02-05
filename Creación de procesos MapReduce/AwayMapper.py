#!/usr/bin/python3
import sys

def parse_csv_line(line):
    # Lógica del parseo manual del csv asumiendo la coma como delimitador
    return line.strip().split(',')

first_line = True  # Eliminamos la primera linea de titulos

for line in sys.stdin:
    if first_line:
        first_line = False
        continue  

    # Parseo manual del CSV
    columns = parse_csv_line(line)

    # Extraemos columnas según su posición
    away_team = columns[4]
    ftr = columns[7]

    # Calculamos puntos basándonos en el valor FTR
    points = 0
    if ftr == 'A':
        points = 3
    elif ftr == 'D':
        points = 1

    # Imprimimos los pares equipo , puntos
    print(f"{away_team}\t{points}")


