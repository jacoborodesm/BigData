#!/usr/bin/python3
import csv
from datetime import datetime
from mrjob.job import MRJob
from mrjob.step import MRStep

class MRPartidosRacha(MRJob):

    def mapper(self, _, line):
        # Convertir la línea de texto a datos CSV
        try:
            # Parse the line as CSV
            row = list(csv.reader([line]))[0]
            
            # Asignar las columnas a variables para mayor claridad
            date_str = row[1]  # La fecha del partido
            home_team = row[3]  # Equipo local
            away_team = row[4]  # Equipo visitante
            full_time_result = row[6]  # Resultado tiempo completo ('H', 'A', 'D')

            # Convertir la fecha de string a objeto datetime para facilitar la ordenación posterior
            date_obj = datetime.strptime(date_str, "%d/%m/%Y")

            # Emitir el resultado para el equipo local
            if full_time_result == 'H':
                yield home_team, (date_obj, 3)  # 3 puntos para victoria
            elif full_time_result == 'A':
                yield home_team, (date_obj, 0)  # 0 puntos para derrota
            else:
                yield home_team, (date_obj, 1)  # 1 punto para empate

            # Emitir el resultado para el equipo visitante
            if full_time_result == 'A':
                yield away_team, (date_obj, 3)  # 3 puntos para victoria
            elif full_time_result == 'H':
                yield away_team, (date_obj, 0)  # 0 puntos para derrota
            else:
                yield away_team, (date_obj, 1)  # 1 punto para empate

        except Exception as e:
            # En caso de error (por ejemplo, una línea malformada), pasar
            pass

if __name__ == '__main__':
    MRPartidosRacha.run()
