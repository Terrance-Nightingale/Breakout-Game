import time
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

player = Paddle()

screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

playing = True
while playing:
    screen.update()

screen.exitonclick()
