from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 36, 'normal')

class Scoreboard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.penup()
        self.setposition(position)
        self.color("white")
        self.goal_score()
        self.hideturtle()

    def goal_score(self):
        self.write(f"{self.score}", False, align= ALIGN, font=FONT )

    def increase_score(self):
        self.clear()
        self.score += 1
        self.goal_score()