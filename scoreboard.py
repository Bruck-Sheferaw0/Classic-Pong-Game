from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.lscore, align='center', font=('courier', 80, 'bold'))
        self.goto(100, 180)
        self.write(self.rscore, align='center', font=('courier', 80, 'bold'))
    def l_score(self):
        self.lscore += 1
        self.update_score()
    def r_score(self):
        self.rscore += 1
        self.update_score()