from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.mov_x = 10
        self.mov_y = 10


    def move(self):
            new_x = self.xcor() + self.mov_x
            new_y = self.ycor() + self.mov_y
            self.goto(new_x, new_y)

    def bounce(self):
        self.mov_y *= -1

    def bounce_x(self):
        self.mov_x *= -1

