import random

class Kloudspot:
    def __init__(self,team=None):
        self.team = team
    
    def show_team(self):
        team = self.team()
        print(f"The team you looking for is {team}")
        print(f"Total number of the team is {team.no_of_people()}")
        

class KloudInsight:
    def no_of_people(self):
        return 20
    def __str__(self):
        return f"Insight"

class KloudVision:
    
    def no_of_people(self):
        return 25

    def __str__(self):
        return "Vision"

class KloudNMS:
    def no_of_people(self):
        return 10
    def __str__(self):
        return "NMS"

class KloudHibred:
    def no_of_people(self):
        return 12
    def __str__(self):
        return "Highbread"

def select_team():
    return random.choice([KloudInsight,KloudVision,KloudNMS,KloudHibred])


if __name__ == "__main__":
    team = select_team()
    klouspot = Kloudspot(team=team)
    klouspot.show_team()