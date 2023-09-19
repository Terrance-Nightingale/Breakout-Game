import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

player = Paddle()
ball = Ball()
ball.seth(225)

screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

playing = True
while playing:
    screen.update()
    ball.move()

    time.sleep(0.09)

screen.exitonclick()
