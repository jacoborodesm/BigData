#!/usr/bin/python3
import sys

def mapper():
    # Leer entrada desde el flujo estándar
    next(sys.stdin)  # Saltar la cabecera del CSV

    goals_dict = {}  # Diccionario para almacenar los goles por equipo

    for line in sys.stdin:
        # Eliminar espacios en blanco de la línea del CSV
        line = line.strip().replace(" ", "")

        row = line.split(',')

        home_team = row[3]
        away_team = row[4]
        home_goals = int(row[5])
        away_goals = int(row[6])

        # Actualizar los goles a favor de cada equipo
        goals_dict[home_team] = goals_dict.get(home_team, 0) + home_goals
        goals_dict[away_team] = goals_dict.get(away_team, 0) + away_goals

    for team, goals in goals_dict.items():
        # Emitir datos de cada equipo: "Equipo" "goles"
        yield (team, goals)

if __name__ == "__main__":
    for output in mapper():
        # Imprimir resultados en el formato "Equipo" "goles"
        print('%s\t%s' % output)


