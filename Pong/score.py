from turtle import Turtle
class Score(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.score=0
        self.goto(pos)
        self.hideturtle()
        self.color("White")
        self.write(self.score, align="center", font=("Arial", 23, "normal"))

    def point(self):
        self.score+=1
        self.clear()
        self.write(self.score, align="center", font=("Arial", 23, "normal"))

    def winner(self):
        self.goto(0,0)
        self.hideturtle()
        self.color("White")
        self.write("", align="center", font=("Arial", 23, "normal"))