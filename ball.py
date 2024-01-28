from turtle import Turtle

class Ball(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.goto(coordinates)
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.05

    def move_ball(self):
        newx = self.xcor() + self.xmove
        newy = self.ycor() + self.ymove
        self.goto(newx,newy)

    # Bounce y value
    def bounce(self):
        self.ymove*=-1

    # bouse x value
    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.99

    def reset(self):
        self.goto(0,0)
        self.bounce_x()

