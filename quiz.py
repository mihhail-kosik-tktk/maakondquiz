# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:26:27 2026

@author: mkosh
"""

import turtle
import pandas
import random
import tkinter as tk

data=pandas.read_csv("maakond.csv")
d= data.to_dict()

screen = turtle.Screen()
screen.bgpic("kaart.gif") 
rng= list(range(15))
random.shuffle(rng)
score=0


for i in rng:
    turtle.pencolor("black")
    print("Next task:")
    x= d['x'][i]
    y= d['y'][i]
    turtle.penup()
    turtle.goto(x, y)  
    turtle.pendown()
    turtle.dot()
    a=input("Mis maakond: ")
    correct= a==d['maakond'][i]
    if correct:
        score+=1
        print("Correct!")
        turtle.write(d['maakond'][i], move=True, align="left", font=("Arial", 10, "normal"))
        turtle.penup()
        turtle.goto(-150, -200)  
        turtle.pendown()
        turtle.dot(60, "white")
        turtle.pencolor("black")
        turtle.write(str(score), move=True, align="left", font=("Arial", 20, "normal"))
    else:
        print("Wrong!")
        turtle.pencolor("red")
        turtle.write(d['maakond'][i], move=True, align="left", font=("Arial", 15, "bold"))
print("Game finished, yoyr score: "+str(score))
turtle.done()