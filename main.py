import random
import time
from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Score
from ball import Ball

screen =Screen()
screen.tracer(0)

l_paddle =Paddle((-385, 0 ))
r_paddle =Paddle((385, 0 ))
score =Score()
ball =Ball()

screen.setup(height=800, width=800)
screen.bgcolor("black")

screen.listen()

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "a")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")


is_game_on =True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    ball.move_ball()

    if ball.ycor() > 390 or ball.ycor() <-390:
        ball.bounce_y()

    if ball.xcor() >350 and ball.distance(r_paddle) < 50 or ball.xcor() <-350 and ball.distance(l_paddle) <50:
        ball.bounce_x()

    if ball.xcor() >390:
        ball.goto_home()
        score.l_point()   

    if ball.xcor() <-390:
        ball.goto_home()
        score.r_point()    


























screen.mainloop()