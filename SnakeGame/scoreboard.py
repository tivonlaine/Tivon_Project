from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        # self.write(f"Score: {self.score}", True, align="center")
        self.write(f"Score: {self.score}", align="center", font=('Arial', 23, 'normal'))

    def point(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 23, 'normal'))

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=('Arial', 23, 'normal'))
