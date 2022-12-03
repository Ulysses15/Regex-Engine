class Task:
    def __init__(self, description, team):
        self.description = description
        self.team = team

    def __add__(self, other):
        comb_description = self.description + '\n' + other.description
        comb_team = self.team + ', ' + other.team
        return Task(comb_description, comb_team)
