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
class Bullet:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = False
        
    def move(self, xpos, ypos):
        if self.isAlive == True:
            self.ypos-=5
        if self.ypos < 0:
            self.isAlive = False
            self.xpos = xpos
            self.ypos = ypos
    
    def draw(self):
        pygame.draw.rect(screen, (250, 250, 250), (self.xpos, self.ypos, 3, 20))
        



class Enemy:
    
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.alive = True
        self.direction = 1
    
    
    def move(self, time):
        
        if timer % 800 == 0:
            self.ypos += 100 #Moves down
            self.direction *=-1 #Flips direction
            return 0 #Resets time to 0
        
        
        if time % 100 == 0:
            self.xpos+=50*self.direction #Moves right 
        
        return time 
            
    
    def draw(self):
        py.draw.rect(screen, (255, 255,255), (self.xpos,self.ypos, 40, 40))
        
            
ballin = []

for i in range(4): #Rows 
    for j in range(10): #Columns
        ballin.append(Enemy(j*60+45, i*60+40))
    
class spaceship:
    def __init__(self, xpos):
        self.xpos = xpos
        self.alive = True
        self.vx = 0
        self.keys = [False, False, False]
        self.LEFT= 0
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

#instantiate bullet object
bullet = Bullet(player.xpos,600)


while True:  
    clock.tick(60)
    timer += 1

    

    #physics section-------------------------------------------


    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    player.update()
    
    for i in range (len(ballin)):
        timer = ballin[i].move(timer)
        ballin[i].draw()
    

    py.display.flip()#this actually puts the pixel on the screen
py.quit()
