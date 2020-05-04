#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:40:23 2020

@author: samabrashoff

pressing 1,2,3...9 changes different colors of the robot (rainbow)
Robot moves with W,A,S,D keys, and Arrow keys.
"""

import pygame
from random import*

#set up colors
BLACK = (0,0,0)
RED = (255,0,0)
PINK = (170,0,50)
YELLOW = (255,255,0)
GREEN = (255,197,0)
BLUE = (0,0,255)
ORANGE = (255,128,0)
GREEEN = (51,255,51)
BBLUE = (51,255,255)
DBLUE = (0,0,255)
PURPLE = (127,0,255)
PINK = (255,0,255)

LT_BLUE = (0, 100, 255)
WHITE = (255,255,255)
GRAY = (0,0,0)
DK_GRAY = (1,85,252)
Color = RED
rSize = 10
size = 500
screen = pygame.display.set_mode((size,size))

run = True
x = size/2 #center position for all robot parts
y = size/2
scale = 1 #variable to adjust when keys are pressed to change size of robot
speed = 6
eye_r = 2
rSize = 10

#Robo features
blink = [GREEN, BLUE, RED, LT_BLUE]
color = choice(blink) #assign a value to color
colorL = choice(blink) #assign a value to color
colorR = choice(blink) #assign a value to color

#Game loop
while run:
    # create exit-on click detection:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            
    #Drawing goes from bottom to top. We'll make our screen white first, then
    #add the robo-parts.    
    screen.fill(WHITE)
    #Pygame draw docs: https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
    Head = pygame.draw.rect(screen,Color,(x-25,y-90,50,50)) 
    Body = pygame.draw.polygon(screen, Color, [(x+35, y-35),(x+45,y+35), (x-45,y+35),(x-35, y-35)])
    L_eye = pygame.draw.circle(screen, BLACK, (int(x-10), int(y-70)),eye_r)
    R_eye = pygame.draw.circle(screen, BLACK, (int(x+10), int(y-70)),eye_r)
    panelLights1 = pygame.draw.circle(screen, DK_GRAY, (int(x+20), int(y-5)),3)
    panelLights2 = pygame.draw.circle(screen, DK_GRAY, (int(x), int(y-5)),3)
    panelLights3 = pygame.draw.circle(screen, DK_GRAY, (int(x-20), int(y-5)),3)

    L_wheel = pygame.draw.circle(screen, BLACK, (int(x-40), int(y+63)),20)
    R_wheel = pygame.draw.circle(screen, BLACK, (int(x+40), int(y+63)),20)
    L_hub = pygame.draw.circle(screen, Color, (int(x-40), int(y+63)),10)
    R_hub = pygame.draw.circle(screen, Color, (int(x+40), int(y+63)),10)
    Track = pygame.draw.ellipse(screen, Color, (int(x-65), int(y+33),130,60),2)

    pygame.display.update() #update all changes to screen

#actual code for robot's movement
    keys = pygame.key.get_pressed() #check for any keys that are pressed        
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += speed
    #I used the video to help me figure out how to change the color of my robot everytime i press a key. https://drive.google.com/file/d/1r_7MQH264sFyofxgyp-ZiXe_Vc6E9H1D/view  
    if keys[pygame.K_1]:
        Color = RED
    if keys[pygame.K_2]:
        Color = YELLOW
    if keys[pygame.K_3]:
        Color = ORANGE  
    if keys[pygame.K_4]:
        Color = GREEEN   
    if keys[pygame.K_5]:
        Color = BBLUE   
    if keys[pygame.K_6]:
        Color = DBLUE   
    if keys[pygame.K_7]:
        Color = PURPLE     
    if keys[pygame.K_8]:
        Color = PINK
    if keys[pygame.K_9]:
        Color = BLACK 
#    if keys[pygame.K_SPACE]:
#        if rSize <=10: 
#            rSize += 10
#        elif rSize > 10:
#            rSize -= 10
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

