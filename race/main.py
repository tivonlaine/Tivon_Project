from turtle import Turtle, Screen
import turtle

timmy=Turtle()
screen=Screen()
screen.listen()

def forward():
    timmy.forward(10)

def back():
    timmy.backward(10)

def right():
    timmy.right(10)

def left():
    timmy.left(10)

def clear():
    timmy.clear()
    timmy.reset()

screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=back)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()