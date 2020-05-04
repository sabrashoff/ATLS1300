#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 08:06:08 2020

@author: samabrashoff
"""

from turtle import*

brickwall = Screen()
brickwall.bgcolor("black")
brickwall.screensize(400,600)
brickwall.update()

brickwall.bgpic("brick-wall.gif")
brickwall.update()
cyanT = Turtle()

cyanT.shape("turtle")
cyanT.color("gold","gold")

pendown()
cyanT.width(8)
cyanT.begin_fill()

cyanT.left(60)
cyanT.forward(100)
cyanT.right(60)
cyanT.forward(100)
cyanT.right(60)
cyanT.forward(100)
cyanT.right(60)
cyanT.forward(100)
cyanT.right(60)
cyanT.forward(100)
cyanT.right(60)
cyanT.forward(100)
cyanT.right(60)
cyanT.forward(100)

cyanT.left(60)
cyanT.forward(100)
cyanT.left(60)
cyanT.forward(100)
cyanT.left(60)
cyanT.forward(100)
cyanT.left(60)
cyanT.forward(100)

cyanT.right(60)
cyanT.forward(100)
cyanT.right(60)
cyanT.forward(100)
cyanT.right(60)
cyanT.forward(100)
cyanT.right(60)
cyanT.forward(100)
cyanT.right(60)
cyanT.forward(100)


cyanT.right(60)
cyanT.forward(100)
cyanT.right(60)
cyanT.forward(100)
cyanT.left(60)
cyanT.forward(100)
cyanT.left(60)
cyanT.forward(100)
cyanT.left(60)
cyanT.forward(100)
cyanT.right(60)
cyanT.forward(100)
cyanT.left(60)
cyanT.forward(100)
cyanT.left(120)


#cyanT.forward(500)
cyanT.up()
cyanT.forward(50)
cyanT.down()
cyanT.forward(50)
cyanT.up()
cyanT.forward(50)
cyanT.down()
cyanT.forward(50)
cyanT.up()
cyanT.forward(50)
cyanT.down()
cyanT.forward(50)
cyanT.up()
cyanT.forward(50)
cyanT.down()
cyanT.forward(50)
cyanT.up()
cyanT.forward(50)
cyanT.up()
cyanT.forward(50)

cyanT.down()

cyanT.color("navyblue")

cyanT.right(120)
cyanT.forward(100)
cyanT.right(60)
cyanT.forward(50)

cyanT.right(90)
cyanT.forward(175)
cyanT.left(90)
cyanT.forward(50)
cyanT.right(60)
cyanT.forward(100)
cyanT.left(60)
cyanT.forward(50)
cyanT.left(90)
cyanT.forward(350)

cyanT.left(90)
cyanT.forward(50)
cyanT.left(60)
cyanT.forward(100)
cyanT.left(120)
cyanT.forward(250)
cyanT.right(90)
cyanT.forward(175)
cyanT.right(90)
cyanT.forward(350)

cyanT.end_fill()

cyanT.hideturtle()


cyanT.done()















