#!/usr/bin/python3

import sys

# Inicializamos variables para rastrear los puntos de cada equipo
current_team = None
current_points = 0
team_points = {}

# Iterar sobre las líneas de entrada
for line in sys.stdin:
    line = line.strip()
    team, date, points = line.split("\t")

    # Convertir los puntos a un entero
    points = int(points)

    # Si el equipo actual es diferente del equipo anterior, emitir el resultado parcial del equipo anterior
    if current_team and current_team != team:
        if current_team not in team_points:
            team_points[current_team] = 0
        team_points[current_team] += current_points

        # Restablecer el valor de current_points para el nuevo equipo
        current_points = 0

    # Actualizar el equipo actual y sumar los puntos del partido actual
    current_team = team
    current_points += points

# Asegurarse de emitir el resultado para el último equipo
if current_team:
    if current_team not in team_points:
        team_points[current_team] = 0
    team_points[current_team] += current_points

# Ordenar el resultado por el valor total_points y emitirlo
sorted_teams = sorted(team_points.items(), key=lambda x: x[1], reverse=True)
for team, total_points in sorted_teams:
    print(f"{team}\t{total_points}")
