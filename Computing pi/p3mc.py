'''
CS 210 Winter 2023 Project 3
Author: Jocelyn Guan
Credit: Help hours
Description: Monte Carlo Simulation - computing pi
'''

import random
import math

random.seed(42)

def pi_mc(num_darts: int) -> float:
    '''
    return the computed appro. of pi

    >>> piMc(10000)
    3.148
    '''

    in_circle = 0

    for i in range(num_darts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x ** 2 + y ** 2)

        if distance <= 1:
            in_circle = in_circle + 1

    pi = in_circle / num_darts * 4

    return pi

print(pi_mc(10000))
