from turtle import Screen, Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.x_positions = [0,20,40]
        self.create_segmnets()
        self.head = self.segments[0]



    def create_segmnets(self):
        for pos in range(3):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(x=self.x_positions[pos],y=0)
            self.segments.append(new_segment)


    def moving_snake(self):

        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num- 1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(20)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)


        self.segments.clear()
        self.create_segmnets()
        self.head = self.segments[0]