import colorgram
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
colorlist=[(243,234,76), (211,158,93), (188,12,69), (111,179,208), (25,116,169), (172,172,31), (221,128,166), (160,78,35), (128,186,146), (10,32,76), (235,73,41), (217,67,108), (31,135,83), (176,48,95), (234,165,194), (79,13,63), (12,55,34), (236,228,6), (29,164,207), (15,42,132), (58,165,95)]
timmy=Turtle()
timmy.speed(0)
color=colorgram.extract("hirst.jpg", 25)

x=-250
y=-220
timmy.penup()
color=0
for i in range(10):
     for j in range(10):
          if color==21:
               color=0
          timmy.goto(x, y)
          timmy.pendown()
          timmy.fillcolor(colorlist[color])
          timmy.begin_fill()
          timmy.circle(10)
          timmy.end_fill()
          timmy.penup()
          x+=50
          color+=1
     x=-250
     y+=50


myscreen=Screen()
myscreen.exitonclick()