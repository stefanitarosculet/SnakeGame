from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
snake.create_segmnets()

food = Food()
score = Score()

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.moving_snake()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_board()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        score.clear()
        score.score_board()
        snake.reset()

screen.exitonclick()