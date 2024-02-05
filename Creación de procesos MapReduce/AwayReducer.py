#!/usr/bin/python3
import sys

# Diccionario para almacenar los puntos de cada equipo
team_points = {}

# Lee la entrada línea por línea desde el stdin
for line in sys.stdin:
    # Elimina espacios en blanco y divide la línea en clave y valor
    line = line.strip()
    team, points = line.split('\t')

    # Agrega los puntos al equipo correspondiente
    team_points[team] = team_points.get(team, 0) + int(points)

# Ordena y muestra la clasificación de puntos obtenidos como visitante
sorted_teams = sorted(team_points.items(), key=lambda x: x[1], reverse=True)
for team, points in sorted_teams:
    print(f"{team}\t{points}")
