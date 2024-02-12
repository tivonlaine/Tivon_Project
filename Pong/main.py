from turtle import Turtle, Screen
from userpaddle import UserPaddle
from ball import Ball
from score import Score
import time
screen=Screen()
screen.setup(width=900, height=500)
screen.bgcolor("Black")
guess=screen.textinput(title="Mode", prompt="Easy or Hard")
screen.tracer(0)
middle=Turtle()
middle.hideturtle()
middle.color("white")
middle.pensize(3)
middle.penup()
middle.speed("fastest")
y=230

middle.goto(0, y)
middle.right(90)
for i in range(23):
    middle.pendown()
    middle.forward(10)
    middle.penup()
    y=y-20
    middle.goto(0,y)
screen.update()

paddle1=UserPaddle((-410,0))
paddle2=UserPaddle((410,0))

score1=Score((-225,165))
score2=Score((225, 165))

screen.update()
screen.tracer(1)

screen.listen()
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")

slow=.03
ball=Ball()
bool=True
hit=True
ball.speed("fastest")
while bool:
    if guess=="hard":
        time.sleep(slow)
    if guess=="easy":
        time.sleep(.03)
    ball.move()
    if ball.xcor()==0:
        hit=True
    if ball.ycor()>240 or ball.ycor()<-235:
        ball.bounce()
    if (ball.distance(paddle2)<50 and ball.xcor()>390 and hit) or (ball.distance(paddle1)<50 and ball.xcor()<-390 and hit):
        hit=False
        ball.hit()
    if ball.xcor()>420:
        score1.point()
        screen.tracer(0)
        ball.goto(0,0)
        if guess == "hard":
            slow=slow/1.2
        ball.hit()
        screen.update()
        screen.tracer(1)
    if ball.xcor()<-420:
        score2.point()
        screen.tracer(0)
        ball.goto(0,0)
        if guess == "hard":
            slow=slow/1.2
        ball.hit()
        screen.update()
        screen.tracer(1)
    if score1.score==5:
        middle.goto(-200,0)
        middle.write("Player 1 wins", align="center", font=("Arial", 23, "normal"))
        bool=False
    if score2.score==5:
        middle.goto(200, 0)
        middle.write("Player 2 wins", align="center", font=("Arial", 23, "normal"))
        bool=False

screen.exitonclick()