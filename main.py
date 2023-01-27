import pygame as py
import random
from math import *
import time
py.init()  
py.display.set_caption("Space Invaders")  # sets the window title
screen = py.display.set_mode((1000, 800))  # creates game screen
screen.fill((0,0,0))
clock = py.time.Clock() #set up clock

timer = 0;


class Enemy:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.alive = True
        
        
    def draw(self):
        if self.alive is True:
             py.draw.rect(screen, (0, 255,0), (self.xpos,self.ypos, 100, 20))
    
    def move(self):
        if timer%100==0:
            self.xpos+=50
            print("moving right")


armada = [] #new list
for i in range (8): #handles rows
    for j in range (4):
        armada.append(Enemy(j*10+50, i*50+50))
        
        
            
class spaceship:
    def __init__(self, xpos):
        self.xpos = xpos
        self.alive = True
        self.vx = 0
        self.keys = [False, False, False]
        self.LEFT=0
        self.RIGHT=1
        self.SPACE = 2

    def move(self):
        for event in py.event.get(): #quit game if x is pressed in top corner
            if event.type == py.QUIT:
                self.alive  = False
            if event.type == py.KEYDOWN: #keyboard input
                if event.key == py.K_SPACE:
                    self.keys[self.SPACE] = True
                if event.key == py.K_LEFT:
                    self.keys[self.LEFT]=True
                elif event.key == py.K_RIGHT:
                    self.keys[self.RIGHT]=True
    # Input KEYUP
            elif event.type == py.KEYUP:
                if event.key == py.K_LEFT:
                    self.keys[self.LEFT]=False
                if event.key == py.K_RIGHT:
                    self.keys[self.RIGHT]=False
                if event.key == py.K_SPACE:
                    self.keys[self.SPACE]= False
    #Shooting
        if self.keys[self.SPACE] == True:
            print("shooting")
            
    #LEFT MOVEMENT
        if self.keys[self.LEFT] == True:
            self.vx=-3
            direction = self.LEFT
    #RIGHT MOVEMENT
        elif self.keys[self.RIGHT]==True:
            self.vx=3
            direction = self.RIGHT
    #turn off velocity
        else:
            self.vx = 0
        #update player position
        self.xpos+=self.vx 
            
    def draw(self):
        if self.alive is True:
            py.draw.rect(screen, (0, 255,0), (self.xpos,750, 100, 20))
            
    def update(self):
        self.draw()
        self.move()
  

#instantiate a spaceship object from the class
player = spaceship(450)

#Enemies
e1 = Enemy(400,400)



while True:  
    clock.tick(60)

    

    #physics section-------------------------------------------
    for i in range(len(armada)):
        armada[i].move()


    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    player.update()
    e1.draw()
    for i in range(len(armada)):
        armada[i].draw()
    

    py.display.flip()#this actually puts the pixel on the screen
py.quit()
