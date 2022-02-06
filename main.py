import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong")
screen.tracer(0)


paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


    if ball.distance(paddle_l) < 25 or ball.distance(paddle_r) < 25:
        ball.bounce_x()


screen.exitonclick()
