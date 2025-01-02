from turtle import Screen
import time
import snake
import food
import scoreboard

screen=Screen()
screen.bgcolor("black")
screen.setup(width=700,height=700)
screen.title("Snake Game")
screen.tracer(0)

food=food.Food()#to generate food
snake=snake.Snake()
score=scoreboard.ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True

while  game_is_on:
    screen.update()#to update the screen when all segments have moved
    time.sleep(0.1)#to produce delay to produce animation effect
    snake.move()#to move the snake

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.food_refresh()
        score.increase_score()
        snake.increase_length()

    #detect collision with wall
    if snake.head.xcor()>340 or snake.head.xcor()<-340 or snake.head.ycor()>330 or snake.head.ycor()<-340:
        game_is_on=False
        score.game_over()

    #detect collision with tail
    for segment in snake.snake_body[1:]: #list starting from 1 till end
        if snake.head.distance(segment)<10:
            game_is_on=False
            score.game_over()

screen.exitonclick()