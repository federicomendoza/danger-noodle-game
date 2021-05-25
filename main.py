from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def play_danger_noodle():
    screen = Screen()
    screen.clearscreen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Danger noodle game")
    screen.tracer(0)

    game_is_on = True
    my_snake = Snake()
    food = Food()

    screen.listen()
    screen.onkey(my_snake.snake_left, "Left")
    screen.onkey(my_snake.snake_right, "Right")
    screen.onkey(my_snake.snake_up, "Up")
    screen.onkey(my_snake.snake_down, "Down")

    score = Scoreboard()
    speed = 0.15
    while game_is_on:
        screen.update()
        time.sleep(speed)
        my_snake.move()
        # detect collision with food
        if my_snake.snake_body[0].distance(food) < 15:
            food.refresh()
            my_snake.enlarge()
            score.increase_score()
            if score.current_score % 3 == 0:
                speed = speed/1.5

        # detect collision with wall
        if my_snake.snake_body[0].xcor() < -290 or my_snake.snake_body[0].xcor() > 290 or my_snake.snake_body[0].ycor() < -290 or my_snake.snake_body[0].ycor() > 280:
            game_is_on = False
            score.game_over()
            score.restart()
            screen.onkey(play_danger_noodle, "space")

        for segment in my_snake.snake_body[2:]:
            if my_snake.snake_body[0].distance(segment) < 10:
                game_is_on = False
                score.game_over()
                score.restart()
                screen.onkey(play_danger_noodle, "space")

    screen.exitonclick()


play_danger_noodle()


