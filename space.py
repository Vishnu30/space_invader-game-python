import turtle
import math
import random
import winsound

#setting up  screen
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("mad-space.gif")

#egister the shape
turtle.register_shape("player.gif")
turtle.register_shape("invader.gif")

#Draw border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#set the score to zero
score=0
#draw the score
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,275)
scorestring="SCORE : %s" %score
score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
score_pen.hideturtle()

#create turtle player
player=turtle.Turtle()
player.color("blue")
player.speed(0)
player.penup()
player.shape("player.gif")
player.setposition(0,-270)
player.setheading(90)


playerspeed=15

#create the enemy
#choose number of enemies
number_enemies=5
enemies=[]
# add enemies to the list
for i in range(number_enemies):
    #create the enemy
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.speed(0)
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    x=random.randint(-200,200)
    y=random.randint(135,250)
    enemy.setposition(x,y)

enemyspeed=2

#create a weapon/bullet    
bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.speed(0)
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed=20

#define bullet state
#fire-bullet is firing
#ready-ready to fire
bulletstate="ready"

#move the player left and right
def move_left():
    x=player.xcor()
    x-=playerspeed
    if x<-280:
        x=-280
    player.setx(x)
def move_right():
    x=player.xcor()
    x+=playerspeed
    if x>280:
       x=280 
    player.setx(x)

#move the bullet
def fire_bullet():
    global bulletstate
    if bulletstate=="ready":
        bulletstate="fire"
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
        #move the bullet to just above the player
        x=player.xcor()
        y=player.ycor()+10 
        bullet.setposition(x,y) 
        bullet.showturtle()
        
def iscollision(t1,t2):
    distance=math.sqrt(math.pow((t1.xcor()-t2.xcor()),2)+math.pow((t1.ycor()-t2.ycor()),2))
    if distance<15:
        return True
    else :
        return False

    
#create keyboard bindings
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")




#main game loop

while True:
    for enemy in enemies:
        
        #move the enemy
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)

        #move the enemy back and down 
        if enemy.xcor()>280:
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
            enemyspeed*=-1

        if enemy.xcor()<-280:
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
            enemyspeed*=-1
            
        #check for collsion between bullet and enemy 
        if iscollision(bullet,enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            #reset the bullet
            bullet.hideturtle()
            bulletstate="ready"
            bullet.setposition(0,-400)
            #reset the enemy
            enemy.setposition(-250,250)
            #update the score
            score+=10
            scorestring="SCORE:%s"%score
            score_pen.clear()
            score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))

        #check for collsion between bullet and enemy    
        if iscollision(enemy,player):
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER")
            break
 
        


   
    #move the bullet
    if bulletstate=="fire":
        y=bullet.ycor()
        y +=bulletspeed
        bullet.sety(y)


    #check to see if the bullet is at the top
    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate="ready"

  



