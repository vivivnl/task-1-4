import doctest
"""
Basketball Player
"""
class Basketball:
    def __init__(self, name, num_games, total_goals):
        """initialise instance variables"""
        self.name = name
        self.num_games = num_games
        self.total_goals = total_goals

    def average_goals_per_game(self):
        global goals 
        goals = self.total_goals/self.num_games
        print("The average score per game for the player", self.name, "is", goals)

player1 = Basketball("Jes", 5, 4)    

player1.average_goals_per_game()
