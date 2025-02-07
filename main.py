import time
from turtle import Screen
from snake import SnakeGame
from food import Food
from score import Scoreboard


def main():
    sc = Screen()
    sc.setup(600, 600)
    sc.bgcolor('black')
    sc.title("Anaconda")
    sc.tracer(0)
    snake = SnakeGame()
    food = Food()
    scoreboard = Scoreboard()
    sc.listen()
    sc.onkey(snake.up, "Up")
    sc.onkey(snake.down, "Down")
    sc.onkey(snake.left, "Left")
    sc.onkey(snake.right, "Right")

    game_on = True
    while game_on:
        sc.update()
        time.sleep(0.1)
        snake.move()

        # Collision detection with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.add_size()
            scoreboard.increase_score()
        # Collision detection with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.score_reset()
            snake.snake_reset()
        # Collision with tail ie head collides with any segment
        for segment in snake.all_turtles[1:]:
            # if segment == snake.head:
            #     pass
            if snake.head.distance(segment) < 10:
                scoreboard.score_reset()
                snake.snake_reset()
    sc.exitonclick()


if __name__ == "__main__":
    main()
