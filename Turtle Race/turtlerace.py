from turtle import Turtle, Screen
import turtle
import random
from random import randint
final=Turtle()
final.hideturtle()
final.color("black")
screen=Screen()
screen.setup(width=500, height=500)
timmy=Turtle("turtle")
bobby=Turtle("turtle")
tommy=Turtle("turtle")
billy=Turtle("turtle")
dobby=Turtle("turtle")
dolly=Turtle("turtle")
molly=Turtle("turtle")
turtles=[timmy, tommy, billy, bobby, dolly, molly, dobby]
colors=["Purple","Green", "Blue","Red","Orange","Pink","Yellow"]
guess=screen.textinput(title="Make your bets!", prompt="Which turtle will win? Pick a color: ")
x=-220
y=-150
num=0
for i in turtles:
    i.speed(0)
    i.color(colors[num])
    i.penup()
    i.goto(x,y)
    y+=50
    num+=1
bool=True
one=True
while bool:
    for i in turtles:
        i.forward(random.randint(0,15))
        if i.xcor()>225 and one:
            winner=i.color()
            bool=False
            one=False
            if guess==winner[0]:
                final.write(f"{winner[0]} won. You win!", align="center", font=('Arial', 23, 'normal') )
            else:
                final.write(f"{winner[0]} won. You lose!", align="center", font=('Arial', 23, 'normal') )


screen.exitonclick()