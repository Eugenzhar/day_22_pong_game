import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard



screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong")
screen.tracer(0)


paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard_r = Scoreboard((40, 230))
scoreboard_l = Scoreboard((-40, 230))


screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with the ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    #Detect collision with the paddle
    if ball.distance(paddle_l) < 50 and ball.xcor() < -320 or ball.distance(paddle_r) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    #Detect l and r paddle misses
    if ball.xcor() < -360:
        ball.reset_position()

        ball.bounce_x()
        scoreboard_r.increase_score()
    elif ball.xcor() > 360:
        ball.reset_position()

        ball.bounce_x()
        scoreboard_l.increase_score()




screen.exitonclick()
