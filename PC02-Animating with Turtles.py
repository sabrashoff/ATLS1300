#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 08:43:36 2020

@author: samabrashoff
"""
from turtle import*

screen = Screen()
screen.setup(700,600)
screen.bgpic("hubble background.gif")
colors = ["red","blue","yellow","purple","green"]

star = Turtle()
star1 = Turtle()
star2 = Turtle()
star3 = Turtle()
star4 = Turtle()
star5 = Turtle()
star6 = Turtle()


star.shape("classic")
star1.shape("classic")
star2.shape("classic")
star3.shape("classic")
star4.shape("classic")
star5.shape("classic")
star6.shape("classic")


for i in range(5):
    star.color(colors[i])
    star1.color(colors[i])
    star2.color(colors[i])
    star3.color(colors[i])
    star4.color(colors[i])
    star5.color(colors[i])
    star6.color(colors[i])
    width(i / 100 +1)
    star.begin_fill()
    star.forward(50)
    star.left(180-36)
    star.forward(50)
    star.end_fill()

turtle = Turtle()
penup()
turtle.goto(100,100)

speed(6)

turtle.shape("classic")
turtle.color("gold","gold")
turtle.width(4)
speed = (3)
for i in range(4):
    turtle.right(90)
    turtle.forward(190)



# i am pretty happy with how my finished code turned out but i could
#not get rid of the thin black line in my design at the end.
    
#starTwo = Turtle()
#starTwo.goto((-25,-87))
#starTwo.shape("classic")
#starTwo.color("red") #(180./255,254/255.,75/255.)) #line, fill
#starTwo.width(4)
#starTWo.turtlesize(2)
#starTwo.speed(0)
#length = 100 #length of side of star
#turn = 180-36
#time.sleep(6)

#star.goto(75,100)
#star.width(4)
#star.turtlesize(1)
#star.speed(6) 



#time.sleep(6)
#star.begin_fill()
#star.forward(length)
#star.left(turn)
#star.color("red")
#star.forward(length)
#star.left(turn)
#star.color("red")
#star.forward(length)
#star.left(turn)
#star.color("white")
#star.forward(length)
#star.left(turn)
#star.forward(length)
#star.left(turn)
#star.end_fill()

#starts drawing new star

#
#star1 = Turtle()
#star1.goto((-125,100))
#star1.shape("triangle")
#star1.color("red") #(180./255,254/255.,75/255.)) #line, fill
#star1.width(4)
#star1.turtlesize(2)
#star1.speed(0)
#length = 100 #length of side of star
#turn = 180-36
#time.sleep(6)

#star1.begin_fill()
#star1.forward(length)
#star1.left(turn)
#star1.color("red")
#star1.forward(length)
#star1.left(turn)
#star1.color("red")
#star1.forward(length)
#star1.left(turn)
#star1.color("white")
#star1.forward(length)
#star1.left(turn)
#star1.forward(length)
#star1.left(turn)
#star1.end_fill()


#start drawing new star

#star2 = Turtle()
#star2.goto((-25,-87))
#star2.shape("triangle")
#star2.color("red") #(180./255,254/255.,75/255.)) #line, fill
#star2.width(4)
#star2.turtlesize(2)
#star2.speed(0)
#length = 100 #length of side of star
#turn = 180-36
#time.sleep(6)

#star2.begin_fill()
#star2.forward(length)
#star2.left(turn)
#star2.color("red")
#star2.forward(length)
#star2.left(turn)
#star2.color("red")
#star2.forward(length)
#star2.left(turn)
#star2.color("white")
#star2.forward(length)
#star2.left(turn)
#star2.forward(length)
#star2.left(turn)
#star2.end_fill()
