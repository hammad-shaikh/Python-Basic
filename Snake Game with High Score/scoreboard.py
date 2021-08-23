from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier",20,"bold")

with open('data.txt') as high:
    score_data = int(high.read())
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.setpos(0,270)
        self.score = 0
        self.high_score = score_data
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT,font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as high:
                high.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()




