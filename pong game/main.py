from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time




screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

tim=Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.goto(x=0,y=-800)
tim.setheading(90)
tim.pensize(5)
tim.color("white")


while tim.ycor()!=800:
    tim.pendown()
    tim.forward(50)
    tim.penup()
    tim.forward(50)





r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up,key="Up")
screen.onkeypress(r_paddle.go_down,key="Down")
screen.onkeypress(l_paddle.go_up,key="w")
screen.onkeypress(l_paddle.go_down,key="s")


game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #detect collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    #detect R paddle misses
    if ball.xcor()>380:
        ball.resetposition()
        scoreboard.l_point()

    # detect L paddle misses
    if ball.xcor() < -380:
        ball.resetposition()
        scoreboard.r_point()
















screen.exitonclick()