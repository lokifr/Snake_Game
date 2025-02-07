from turtle import Turtle


class SnakeGame:
    def __init__(self):
        self.all_turtles = []
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        for position in self.starting_positions:
            self.extend(position)

    def extend(self, position):
        new_turtle = Turtle(shape='square')
        new_turtle.penup()
        new_turtle.color('white')
        new_turtle.goto(position)
        self.all_turtles.append(new_turtle)

    def add_size(self):
        self.extend(self.all_turtles[-1].position())

    def move(self):
        for seg_num in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[seg_num - 1].xcor()
            new_y = self.all_turtles[seg_num - 1].ycor()
            self.all_turtles[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def snake_reset(self):
        for i in self.all_turtles:
            i.goto(1000, 1000)
        self.all_turtles.clear()
        self.create_snake()
        self.head = self.all_turtles[0]