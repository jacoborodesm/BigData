#!/usr/bin/python3
import sys

# Iterar sobre las líneas de entrada
for line in sys.stdin:
    line = line.strip()
    # Dividir la línea en campos
    fields = line.split(",")

    if len(fields) == 75:
        # Obtener el nombre del equipo local y visitante
        home_team = fields[3]
        away_team = fields[4]

        # Obtener el resultado final (FTR)
        ftr = fields[7]

        # Inicializar los puntos para el equipo local y visitante
        home_points = 0
        away_points = 0

        # Calcular los puntos en función del resultado final (FTR)
        if ftr == 'H':
            home_points += 3
        elif ftr == 'D':
            home_points += 1
            away_points += 1
        elif ftr == 'A':
            away_points += 3

        # Emitir el nombre del equipo local y visitante junto con los puntos
        print(f"{home_team}\t{home_points}")
        print(f"{away_team}\t{away_points}")




