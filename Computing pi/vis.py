'''
CS 210 Winter 2023 Project 3
Author: Jocelyn Guan
Credit: Help hours
Description: Visualization of the MC - computing pi
'''

import random
import math
from turtle import *

def setup():
    '''
    '''
    Screen()
    setworldcoordinates(-7, -7, 7, 7)

    up()
    setpos(-1, 0)
    down()
    setpos(1, 0)
    up()
    setpos(0, 1)
    down()
    setpos(0, -1)

    return

def showMontepi(num_darts):
    '''
    '''

    setup()
    in_circle = 0
    up()

    for i in range(num_darts):
        x = random.uniform(-1, 1) # random.random()
        y = random.uniform(-1 ,1)
        
        d = math.sqrt(x**2 + y**2)
        setpos(x,  y)
        
        if d <= 1:
            in_circle = in_circle + 1 
            pencolor("blue")
        else:
            pencolor("red")
        
        dot()

    pi = in_circle / num_darts * 4

    return

def main():
    '''

    '''

    showMontepi(200)
    hideturtle()
    speed(0)

    return

main()