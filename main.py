# Today is my day 22 of learning python in 100 days , my days objective is to create a pong game.

from turtle import Screen
from project_day_22.paddle_day import Paddle
from project_day_22.ball_day import Ball
from project_day_22.Scorecard import Scoreboard
import time

ball = Ball()
screen = Screen()
scoreboard = Scoreboard()
paddle = Paddle((0,0))
paddle.shapesize(stretch_wid=30, stretch_len=0.1)
POS = [(350,0), (-350,0)]
move_pace = 0.1

screen.setup(width = 800 , height = 600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

r_paddle = Paddle(POS[0])
l_paddle = Paddle(POS[1])

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")# do not need to add parenthesis when passing function as a parameter.
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_on = True
while game_on:
    time.sleep(move_pace)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        move_pace -= 0.01


    if ball.xcor() > 350 :
        ball.game_reset()
        move_pace = 0.1
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    if ball.xcor() < -350 :
        ball.game_reset()
        move_pace = 0.1
        scoreboard.r_point()
        scoreboard.update_scoreboard()


screen.exitonclick()
