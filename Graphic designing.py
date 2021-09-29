# space invaders by ps
import turtle
import os
import math
import random

#setting up the game screen
w=turtle.Screen()
w.bgcolor('black')
w.title('SPACE INVADERS')

#drawing game border
b_pen=turtle.Turtle()
b_pen.speed(0)
b_pen.color('black')
b_pen.penup()
b_pen.setposition(-300,-300)
b_pen.pendown()
b_pen.pensize(3)
for side in range(4):
    b_pen.fd(600)
    b_pen.lt(90)
b_pen.hideturtle()

#creating player turtle
p=turtle.Turtle()
p.color('blue')
p.shape('triangle')
p.penup()
p.speed(0)
p.setposition(0,-250)
p.setheading(90)

pspeed=15

#choose no. of enemies
no_of_enemy=10

#emty list of enemies
enemies=[]

#add enemies to list
for i in range(no_of_enemy):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color('red')
    enemy.shape('square')
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-200,200)
    y=random.randint(100,250)
    enemy.setposition(x,y)

enemyspeed=5

#create the player's bullet
bul=turtle.Turtle()
bul.color('yellow')
bul.shape('triangle')
bul.penup()
bul.speed(0)
bul.setheading(90)
bul.shapesize(0.25,0.25)
bul.hideturtle()

bulspeed=20

#bullet state
bulstate='ready'

#player movements

#move player left and right
def move_left():
    x=p.xcor()
    x -= pspeed
    if x<-600:
        x=600
    p.setx(x)

def move_right():
    x=p.xcor()
    x += pspeed
    if x>600:
        x=600
    p.setx(x)

def fire_bullet():
    #declare bulstate as a global if it needs change
    global bulstate
    if bulstate=='ready':
        bulstate='fire'
        #move the bullet to just above the player
        x=p.xcor()
        y=p.ycor()+10
        bul.setposition(x,y)
        bul.showturtle()
def iscollision(t1,t2):
    dist=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if dist<15:
        return True
    else:
        return False

#creating keyboard bindings
turtle.listen()
turtle.onkey(move_left,'Left')
turtle.onkey(move_right,'Right')
turtle.onkey(fire_bullet,'space')

#main game loop
while True:
    for enemy in enemies:
        #move the enemy
        x=enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #move  enemy back and down
        if enemy.xcor()>600:
            #move all enemies down
            for e in enemies:
                y=e.ycor()
                y=-40
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor()<-600:
            for e in enemies:
                y=e.ycor()
                y -=40
                e.sety(y)
            enemyspeed *= -1

        #check for collision
        if  iscollision(bul,enemy):
            #reset the bullet
            bul.hideturtle()
            bulstate='ready'
            bul.setposition(0,-400)
            #reset the enemy
            enemy.setposition(-200,250)
            #reset the enemy
            x=random.randint(-200,200)
            y=random.randint(100,250)
            enemy.setposition(x,y)

        if iscollision(p,enemy):
            p.hideturtle()
            enemy.hideturtle()
            print('GAME OVER')
            break
    #move the bullet
    if bulstate=='fire':
        y=bul.ycor()
        y += bulspeed
        bul.sety(y)

    #check if bullet has gone to the top
    if bul.ycor()>275:
        bul.hideturtle()
        bulstate='ready'

