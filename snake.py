from turtle import Turtle

BODY_SECTIONS = 6
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.last_direction = self.snake_body[0].heading()

    def create_snake(self):
        y_zero = 0
        x_zero = -20
        for i in range(BODY_SECTIONS):
            self.snake_body.append(Turtle(shape="square"))
            self.snake_body[i].color("white")
            self.snake_body[i].shapesize(stretch_wid=0.9, stretch_len=0.9)
            self.snake_body[i].penup()
            self.snake_body[i].goto(x=x_zero, y=y_zero)
            x_zero -= 20

    def move(self):
        for section_index in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[section_index - 1].xcor()
            new_y = self.snake_body[section_index - 1].ycor()
            self.snake_body[section_index].goto(new_x, new_y)
        self.snake_body[0].forward(20)
        self.last_direction = self.snake_body[0].heading()

    def snake_up(self):
        if self.snake_body[0].heading() != DOWN and self.last_direction != DOWN:
            self.snake_body[0].setheading(UP)

    def snake_down(self):
        if self.snake_body[0].heading() != UP and self.last_direction != UP:
            self.snake_body[0].setheading(DOWN)

    def snake_left(self):
        if self.snake_body[0].heading() != RIGHT and self.last_direction != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def snake_right(self):
        if self.snake_body[0].heading() != LEFT and self.last_direction != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def enlarge(self):
        self.snake_body.append(Turtle(shape="square"))
        new_part_i = len(self.snake_body)-1
        position = self.snake_body[new_part_i-1].position()
        print(position)
        self.snake_body[new_part_i].shapesize(stretch_wid=0.9, stretch_len=0.9)
        self.snake_body[new_part_i].color("white")
        self.snake_body[new_part_i].penup()
        self.snake_body[new_part_i].goto(position)

