from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake=Snake()
food=Food()
scoreb=Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


bool=True

while bool:
    screen.update()
    time.sleep(.1)
    snake.move()
#   food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreb.point()

    # hit wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        bool=False
        scoreb.gameover()
    #collision with tail
    for turtle in snake.turtles[1:]:
        if snake.head.distance(turtle)<15:
            bool=False
            scoreb.gameover()




screen.exitonclick()
