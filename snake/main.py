from turtle import Screen , Turtle 
from snake import Snake ,Food
from scoreboard import Scoreboard
import time
import pygame 
# creat widget 
window=Screen()
window.setup(700,700)
window.bgcolor("black")
window.tracer(0)
# preparing sounds 
pygame.mixer.init()
pygame.mixer.music.load("assets/bgmusic.mp3")

eat =pygame.mixer.Sound("assets/eat.mp3")

level_up=pygame.mixer.Sound("assets/level_up.mp3")

Game_Over=pygame.mixer.Sound("assets/game_over.mp3")

#creat the snake and select the direction
sam=Snake()
window.update()
window.listen()
window.onkey(sam.go_up,"Up")
window.onkey(sam.go_down,"Down")
window.onkey(sam.go_left,"Left")
window.onkey(sam.go_right,"Right")
#making the move endless
writer=Turtle()
#writer.sh
writer.hideturtle()
writer.color("yellow")
writer.penup()
writer.goto(320,320)
writer.pendown()
writer.pensize(5)
writer.goto(320,-320)
writer.goto(-320,-320)
writer.goto(-320,320)
writer.goto(320,320)
apple=Food()
piriod=0.12
scorer=Scoreboard()
def game_over():
        for i in sam.body:
            i.hideturtle()
            i.color("yellow")
        window.update()
        window.bgcolor("red")
        writer.goto(0,0)
        writer.pendown()
        writer.write(f"Game Over \n your score is :{sam.score()} \n Play again?(y/n)",align="center",font=("arial",36,"bold"))
        pygame.mixer.music.stop()
        Game_Over.play()
pygame.mixer.music.play(-1,0.0)

game_on=True
while game_on:  
    sam.move(20)
    time.sleep(piriod)
    if sam.head.distance(apple) < 19 :
       
        scorer.increase()
        scorer.update_scoreboard()
        apple.appear()
        sam.eating()
        
        
        if (sam.score())%4 == 0:
            level_up.play()
            if piriod <=0.02:
                pass
            else:
                piriod=piriod  - 0.02 
        else:
            eat.play() 
#gameover 
    if sam.body[0].xcor() > 305 or sam.body[0].xcor() < -305 or sam.body[0].ycor() > 305 or sam.body[0].ycor() < -305 :
        
        writer.penup()
        window.update()
        game_over()
        
        
        scorer.save_score()
        game_on=False
    for i in range(2,len(sam.body)) :
        if sam.head.distance(sam.body[i]) <10 :
            game_over()     
            scorer.save_score() 
            game_on=False
    
    window.update()


window.exitonclick() 