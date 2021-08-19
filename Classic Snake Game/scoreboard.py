from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier",20,"bold")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.setpos(0,270)
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()




