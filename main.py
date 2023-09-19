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

    # Detect if ball hits wall/paddles
    x_cor = ball.xcor()
    y_cor = ball.ycor()
    if x_cor > 280 or x_cor < -280:
        ball.bounce()
    elif ball.distance(player) < 50:
        ball.bounce()

    # Keep track of score
    if y_cor < -380:
        ball.reset()

    time.sleep(0.09)

screen.exitonclick()
