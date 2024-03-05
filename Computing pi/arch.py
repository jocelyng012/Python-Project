'''
CS 210 Winter 2023 Project 3
Author: Jocelyn Guan
Credit: Help hours
Description: The Archimedes Method - computing pi
'''

import math

def pi_arch(num_sides: int) -> float:
    '''
    return the computed appro. of pi

    >>> piArch(100)
    3.141075907812829
    '''
    inner_angle_b = 360.0 / num_sides
    half_angle_a = inner_angle_b / 2
    one_half_side_s = math.sin(math.radians(half_angle_a))
    side_s = one_half_side_s * 2
    polygon_circumference = num_sides * side_s
    pi = polygon_circumference / 2

    return pi

