#!/usr/bin/python3
import sys

def reducer():
    max_goals = float('-inf')
    min_goals = float('inf')
    max_team = ""
    min_team = ""

    for line in sys.stdin:
        team, goals = line.strip().split('\t')
        goals = int(goals)

        # Encontrar el equipo con más goles y el equipo con menos goles
        if goals > max_goals:
            max_goals = goals
            max_team = team
        if goals < min_goals:
            min_goals = goals
            min_team = team

    # Calcular la diferencia de goles entre el equipo con más y menos goles
    diff_goals = abs(max_goals - min_goals)

    output_text = f"{max_team} vs {min_team}"

    yield (output_text, diff_goals)

if __name__ == "__main__":
    for output in reducer():
        # Imprimir resultados en el formato "Equipo con más goles vs equipo con menos goles" "diferencia de goles XX"
        print('%s\t%s' % output)

