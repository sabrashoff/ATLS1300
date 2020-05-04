#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:20:31 2020

@author: samabrashoff
"""

'''
Elliott Cutcliffe, Claire Kennedy, Sam Abrashoff, Jack Ahern
Generative Art Gallery
April 27,2020
Psuedocode:
 Draws random different shapes and colors
 Pulls from a random list of colors and numbers (for lengths of different shapes, and starting coordinates)
 User can press the RETURN key to make the loop stop for 5 seconds, then the loop will continue to cycle through all the random shapes
 
 Wrote out all imports
 Came up with a bunch of different color values
 Came up with our random length and random coordinate variables
 Defined a bunch of shape functions
 Put all our functions into a list
 Called our funcations from the list in our while loop and organized them to start in rows of 3 and columnns of 3 
 Added the function for the RETURN key to stop the while loop for 5 seconds
 Added a sleep time for 0.1 so the user can see the shapes as they go by
'''


#importing 
import pygame
from random import *
import random
import time

#variables
blue = (177,221,241) #pallette selected from coolors.co to account for the colorblind!
white = (255,255,255) 
red = (163,22,33) 
yellow = (100,100,0)
green = (0,255,0)
orange = (150,150,0)
purple = (100,0,200)
sapphire = (62,27,233)
brightorange = (246,114,19)
hotpink = (243,0,255)
spanishblue = (1,111,185)
navyblue = (5,0,117)
mauve = (226,194,255)
tiffanyblue = (46,196,182)
cyan = (203,243,240)
keylime = (231,245,158)
golden = (255,215,0)
deepskyblue = (0,191,255)
tryanpurple = (112,5,72)
neonblue = (84,101,255)
magenta = (255,25,141)
#random stuff
randomLength = randint(20,150)
randomCoord = randint(5,25)


size = 600
run = True

#setting up screen
screen = pygame.display.set_mode((size,size))
screen.fill(white)


colors = [yellow, blue, white, purple, red, green, orange, sapphire, brightorange,hotpink,spanishblue,navyblue,mauve,tiffanyblue,cyan,keylime,golden,deepskyblue,tryanpurple,neonblue,magenta]
#color = random.choice(colors)

#functions that draw shapes
def myCircle(x,y):
    pygame.draw.circle(screen, random.choice(colors), (int(x+100), int(y+100)),randomLength)  
def myRect(x,y):
    pygame.draw.rect(screen, random.choice(colors),(x+randomCoord,y+randomCoord,randomLength,randomLength))
def myTriangle(x,y):
    pygame.draw.polygon(screen, random.choice(colors),((x+100,y+5),(x+5,y+195),(x+195,y+195)))
def myDiamond(x,y):
    pygame.draw.polygon(screen, random.choice(colors),((x+100,y+5),(x+5,y+100),(x+100,y+195),(x+195,y+100)))
def myLightning(x,y):
    pygame.draw.polygon(screen, random.choice(colors),((x+5,y+195),(x+195,y+5),(x+100,y+5)))
def myUpsideDownTriangle(x,y):
    pygame.draw.polygon(screen, random.choice(colors),((x+5,y+5),(x+100,y+195),(x+195,y+5)))
def myStopSign(x,y):
    pygame.draw.polygon(screen, random.choice(colors),((x+52,y+5),(x+148,y+5),(x+195,y+52),(x+195,y+148),(x+148,y+195),(x+52,y+195),(x+5,y+148),(x+5,y+52)))
def myLightning2(x,y):
    pygame.draw.polygon(screen, random.choice(colors),((x+5,y+5),(x+100,y+5),(x+195,y+195)))
def myStar(x,y):
    pygame.draw.polygon(screen, random.choice(colors),((x+100,y+5),(x+120,y+50),(x+195,y+50),(x+130,y+100),(x+180,y+195),(x+100,y+130),(x+20,y+195),(x+70,y+100),(x+5,y+50),(x+80,y+50)))
def myPacman(x,y):
    pygame.draw.circle(screen, random.choice(colors), (int(x+100), int(y+100)),95) 
    pygame.draw.polygon(screen, white,((x+100,y+100),(x+195,y+40),(x+195,y+140)))
def myRedStar(x,y):
    pygame.draw.polygon(screen, random.choice(colors),((x+100,y+5),(x+120,y+50),(x+195,y+50),(x+130,y+100),(x+180,y+195),(x+100,y+130),(x+20,y+195),(x+70,y+100),(x+5,y+50),(x+80,y+50)))
def myRedCircle(x,y):
    pygame.draw.circle(screen, random.choice(colors), (int(x+100), int(y+100)),95) 
def myRedCross(x,y):
    pygame.draw.polygon(screen, random.choice(colors),((x+66,y+5),(x+132,y+5),(x+132,y+195),(x+66,y+195)))
    pygame.draw.polygon(screen, random.choice(colors),((x+5,y+66),(x+5,y+132),(x+195,y+132),(x+195,y+66)))
    



#list of my functions/shapes
myFuncs = [myCircle,myRect,myTriangle,myDiamond,myLightning,myUpsideDownTriangle,myStopSign,myLightning2,myStar,myPacman,myRedStar,myRedCircle,myRedCross]


#calls the functions fo drawing the shapes
#when the retrun key is pressed the final gallery is shown 
while run: 
    screen.fill(white)
    time.sleep(.1) #slows down the visual so the user can see the shapes going by 

    for row in range (3): #calls 9 random functions/shapes from our myFuncs list
        for column in range (3):
            choice(myFuncs)(column*200,row*200)
          
        
    keys = pygame.key.get_pressed() #when the RETURN button is pressed, the moving visuals stop for 5 seconds
    if keys[pygame.K_RETURN]:
        time.sleep(5)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False    
            
    pygame.display.update()
    