from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.color('white')
        self.shape("square")
        self.shapesize(5,1)
        self.penup()
        self.coordinates = coordinates
        self.goto(coordinates)

    def Up(self):
        ycor = self.ycor() + 20
        self.goto(self.xcor(), ycor)

    def Down(self):
        ycor = self.ycor() - 20
        self.goto(self.xcor(), ycor)
