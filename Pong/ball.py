from turtle import Turtle, colormode
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.xmove=20
        self.ymove=20

    def move(self):
        self.penup()
        x = self.xcor() + self.xmove
        y = self.ycor() + self.ymove
        self.goto(x,y)

    def bounce(self):
        self.ymove*=-1

    def hit(self):
        self.xmove*=-1

