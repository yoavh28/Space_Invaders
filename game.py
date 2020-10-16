#Space Invaders - Part 1
import pip
import turtle
import os
import math
import random
import time

import pygame
from pygame import mixer # Load the required library
pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()

#Situation   In game -> 1   Lose -> 0
situation=1

#Set up screen
wn=turtle.Screen()
#change to full screen
wn.screensize()
wn.setup(width = 1.0, height = 1.0)
wn.bgcolor("Black")
wn.title("Space Invaders")
wn.bgpic("SpaceInvaders_background.gif")

#Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

#Draw border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for size in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set score to 0
score=0
#Draw the score
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,270)
scorestring="Score: " +str(score)
score_pen.write(scorestring,False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()



#Create the player turtle
player=turtle.Turtle()
player.hideturtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
player.showturtle()
playerspeed=15



#Choose a number of enemies
number_of_enemies=5
#Create an empty list of enemies
enemies=[]
#Add enemies to the list
for i in range(number_of_enemies):
    #Create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    # Create the enemy
    enemy.hideturtle()
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-200,200)
    y=random.randint(-200, 200)
    enemy.setposition(x,y)
    enemy.showturtle()

enemyspeed = 2



#Create the player's bullet
bullet=turtle.Turtle()
bullet.hideturtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bulletspeed=20

#Define bullet state
#Ready - ready to fire
#fire - bullet is firing
bulletstate="ready"


#Move the player left and right

def move_left():
    x=player.xcor()
    x-=playerspeed
    if(x<-280):
        x=-280
    player.setx(x)

def move_right():
    x=player.xcor()
    x+=playerspeed
    if(x>280):
        x=280
    player.setx(x)

def fire_bullet():
    #Declare bulletstate as a global if it needs a change
    global bulletstate
    if(bulletstate=="ready"):
        pygame.mixer.music.load("Laser Gun Sound Effect.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(1)
        bulletstate="fire"
        #Move the bullet to just above the player
        x=player.xcor()
        y=player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if(distance<25):
        return True
    else:
        return False

#Create keyboards bindings
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")

#Main game loop
while (situation==1):
    for enemy in enemies:
        #Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        #Move the enemy back and down
        if(enemy.xcor()>280):
            #Move all enemies down
            for e in enemies:
               y=e.ycor()
               y-=40
               e.sety(y)
            #Change enemy direction
            enemyspeed*=-1

        if(enemy.xcor()<-280):
            #Move all enemies down
            for e in enemies:
               y = e.ycor()
               y -= 40
               e.sety(y)
            #Change enemy direction
            enemyspeed *= -1
         #Check for collision between the bullet and the enemy
        if (isCollision(bullet, enemy)):
               # Reset the bullet
               bullet.hideturtle()
               bulletstate = "ready"
               bullet.setposition(0, -400)
               # Reset the enemy
               x = random.randint(-200, 200)
               y = random.randint(-200, 200)
               enemy.setposition(x, y)
               pygame.mixer.music.stop()
               #Update the score
               score+=10
               scorestring = "Score: " + str(score)
               score_pen.clear()
               score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        if (isCollision(player, enemy)or(enemy.ycor()<=-220)):
               pygame.mixer.music.load("Gameover Sound Effect.mp3")
               pygame.mixer.music.set_volume(0.5)
               pygame.mixer.music.play(1)
               player.hideturtle()
               bullet.hideturtle()
               for enemy in enemies:
                   enemy.hideturtle()
               turtle.hideturtle()
               turtle.color("white")
               turtle.write("GAME OVER", move=False, align="center", font=("Arial", 26, "normal"))
               time.sleep(1)
               pygame.mixer.music.stop()
               situation=0
    #Move the bullet
    if(bulletstate=="fire"):
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)

    #Check to see if the bullet has gone to the top
    if (bullet.ycor()>275):
        bullet.hideturtle()
        bulletstate="ready"



turtle.done()
delay=raw_input("Press enter to finish")