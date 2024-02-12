from turtle import Turtle
class UserPaddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)
        self.penup()
        self.goto(pos)
    def up(self):
        y=self.ycor()+35
        self.goto(self.xcor(),y)

    def down(self):
        y=self.ycor()-35
        self.goto(self.xcor(), y)



