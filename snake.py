import turtle
MOVING_STEPS=20

class Snake:
    def __init__(self):
        self.snake_body=[]
        self.create_snake()
        self.head=self.snake_body[0]

    def create_snake(self):
        #initializing snake
        starting_positions=[(0,0),(-20,0),(-40,0)]
        for position in starting_positions:
            segment=turtle.Turtle()
            if position==(0,0):
                segment.shape("triangle")
            else:
                segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.snake_body.append(segment)

    def move(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            pos_x = self.snake_body[segment - 1].xcor()  # taking pos of previous segment
            pos_y = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(pos_x, pos_y)
        self.snake_body[0].forward(MOVING_STEPS) #moving the snake by 20 steps

    def up(self):
        direction=self.snake_body[0].heading()
        if not direction==270:
            self.snake_body[0].setheading(90)

    def down(self):
        direction = self.snake_body[0].heading()
        if not direction==90:
            self.snake_body[0].setheading(270)

    def left(self):
        direction = self.snake_body[0].heading()
        if not direction==0:
            self.snake_body[0].setheading(180)

    def right(self):
        direction = self.snake_body[0].heading()
        if not direction==180:
            self.snake_body[0].setheading(0)

    def increase_length(self):
        pos_x = self.snake_body[-1].xcor()  # taking pos of previous segment
        pos_y = self.snake_body[-1].ycor()
        segment = turtle.Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segment.goto(pos_x,pos_y)
        self.snake_body.append(segment)