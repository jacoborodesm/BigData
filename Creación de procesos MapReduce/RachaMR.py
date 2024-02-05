#!/usr/bin/python3

from mrjob.job import MRJob
from mrjob.step import MRStep
from collections import deque
import heapq

class LaLigaMR(MRJob):

    def mapper(self, _, line):
        # Splitting the line into components
        components = line.split(',')
        date, _, _, home_team, away_team, _, _, result, *rest = components
        
        if home_team == "HomeTeam":  # Skip the header
            return
        
        # Prepare match information for sorting and result calculation
        if result == 'D':  # Draw
            home_result = away_result = '1'
            home_points = away_points = 1
        elif result == 'H':  # Home win
            home_result, away_result = '3', '0'
            home_points, away_points = 3, 0
        else:  # Away win
            home_result, away_result = '0', '3'
            home_points, away_points = 0, 3

        yield (home_team, date), (home_points, home_result)
        yield (away_team, date), (away_points, away_result)

    def reducer_init(self):
        self.team_streaks = {}  # Initialize a dictionary to store team streaks

    def reducer(self, team_date, values):
        team, date = team_date
        if team not in self.team_streaks:
            self.team_streaks[team] = {'points': 0, 'last_five': deque(maxlen=5)}

        for points, result in values:
            # Update points and last five matches
            self.team_streaks[team]['points'] += points
            self.team_streaks[team]['last_five'].appendleft(result)  # Append on the left for correct order

        # Emit the team's total points and the results of the last five matches
        # Use a common key (e.g., None or 'all') to gather all data in the final reducer
        yield None, (self.team_streaks[team]['points'], team, list(self.team_streaks[team]['last_five']))

    # Final reducer to sort by points and yield sorted results
    def final_reducer(self, _, team_data):
        # Sorting all teams by points in descending order
        sorted_teams = sorted(team_data, reverse=True)  # Sorts based on the first element of the tuple (points)
        for total_points, team, last_five in sorted_teams:
            yield team, (total_points, last_five)

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer_init=self.reducer_init,
                   reducer=self.reducer),
            MRStep(reducer=self.final_reducer)  # Adding a final step for sorting
        ]

if __name__ == '__main__':
    LaLigaMR.run()

