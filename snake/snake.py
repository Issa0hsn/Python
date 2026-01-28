from turtle import Turtle 
from random import randint
#snake class 

class Snake ():
    def __init__(self):
       
       self.body=[]
       self.creat_snake()
       self.head=self.body[0]
    def creat_snake(self):
            for i in range(5):
                new_part=Turtle(shape="square")
                new_part.color("white")
                new_part.penup()
                new_part.goto(-20*i,0)
                self.body.append(new_part)

    def move(self,step):
        for i in range(len(self.body) - 1,0 ,-1):

            self.body[i].goto((self.body[i-1].pos()))
        self.body[-1].showturtle()
        self.head.forward(step)
    def go_down(self):
        if self.head.heading() !=90:
            self.head.setheading(270)               
    def go_up(self):
          if self.head.heading() !=270:
            self.head.setheading(90)
    def go_left(self):
        if self.head.heading() !=0:
            self.head.setheading(180)        
    def go_right(self):
        if self.head.heading() !=180:
            self.head.setheading(0)  
    def eating(self):
        part=Turtle(shape="square")
        part.color("white")
        part.penup()
        part.hideturtle()
        self.body.append(part)
    def score(self):
        return len(self.body) -5
    
#Food class 
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.penup()
        self.appear()
    def appear(self)    :
        self.goto(randint(-14,14)*20,randint(-14,14)*20)
    def eated(self):
        self.hideturtle()
    pass