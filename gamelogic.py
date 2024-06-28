class GameLogic:
    def __init__(self, score=0, lives=3):
        self.score = score
        self.lives = lives

    def update_score(self, points):
        self.score += points
        new_ball = False
        if self.score == 100:
            new_ball = True
        return new_ball

    def lose_life(self):
        self.lives -= 1

    def is_game_over(self):
        return self.lives <= 0

    def reset_game(self):
        self.score = 0
        self.lives = 3
