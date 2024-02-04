from turtle import Turtle
import turtle
class Snake:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.turtles = []
        self.createsnake()
        self.head=self.turtles[0]
    def createsnake(self):
        for i in range(3):
            timmy = Turtle("square")
            self.turtles.append(timmy)
            timmy.color("white")
            timmy.penup()
            timmy.speed(0)
            timmy.goto(self.x, self.y)
            self.x -= 21

    def move(self):
        for turtle in range(len(self.turtles) - 1, 0, -1):
            prevx = self.turtles[turtle - 1].xcor()
            prevy = self.turtles[turtle - 1].ycor()
            self.turtles[turtle].goto(prevx, prevy)
        self.head.forward(20)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)

    def extend(self):
        timmy = Turtle("square")
        self.turtles.append(timmy)
        timmy.color("white")
        timmy.penup()
        timmy.speed(0)
        timmy.goto(self.x, self.y)
        self.x -= 21
