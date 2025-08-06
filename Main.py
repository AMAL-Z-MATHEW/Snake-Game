from turtle import *

from food import Food
from scoreboard import Score
from snake import *
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")
screen.bgcolor("black")
screen.tracer(0)
snake=Snake()
food=Food()
score=Score()
i=0
game_on=True
while game_on:
    score.refresh(i)
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
      food.refresh()
      snake.extend()
      i+=1
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_on=False
        score.game_over()
    for segment in snake.snake[1:]:
        if snake.head.distance(segment)<10:
            game_on = False
            score.game_over()












screen.exitonclick()