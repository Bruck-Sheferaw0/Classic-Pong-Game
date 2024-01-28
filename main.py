from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
score = Score()
import time
# screen setup
screen = Screen()
screen.setup(800,600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)
# right and left paddle setup and controls
right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
# object ball
ball = Ball((0,0))




screen.listen()
screen.onkeypress(right_paddle.Up, "Up")
screen.onkeypress(right_paddle.Down, "Down")
screen.onkeypress(left_paddle.Up, "w")
screen.onkeypress(left_paddle.Down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    # detect upper wall collision
    if ball.ycor() > 298 or ball.ycor() < -298:
        ball.bounce()
    # detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 410:
        ball.reset()
        score.l_score()

    elif ball.xcor() < -410:
        ball.reset()
        score.r_score()












screen.exitonclick()