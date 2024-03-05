'''
CS 210 Winter 2023 Project 3
Author: Jocelyn Guan
Credit: Help hours
Description: Putting all together - computing pi
'''

import math
import random

random.seed(42)

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


def pi_wallis(num_pairs: int) -> float:
    '''
    return the computed appro. of pi

    >>> piWallis(210)
    3.1378637641747664
    '''

    acc = 1
    num = 2

    for pair in range(num_pairs):
        left_term = num / (num - 1)
        right_term = num / (num + 1)

        acc =  acc * left_term * right_term

        num =  num + 2

    pi = acc * 2

    return pi


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


def all_pi(err_tol: float) -> list:
    '''
    '''

    tolerance = err_tol

    acc_arch = 6
    acc_wallis = 6
    acc_mc = 7

    arch_pi = abs(math.pi - pi_arch(acc_arch))
    wallis_pi = abs(math.pi - pi_wallis(acc_wallis))
    mc_pi = abs(math.pi - pi_mc(acc_mc))

    # Arch
    while abs(math.pi - pi_arch(acc_arch)) > tolerance:
        arch_pi = abs(math.pi - pi_arch(acc_arch))
        acc_arch += 1

    print(f'Archimedes: num_sides = {acc_arch} Differs by {arch_pi}')
    
    # Wallis
    while abs(math.pi - pi_wallis(acc_wallis)) > tolerance:
        wallis_pi = abs(math.pi - pi_wallis(acc_wallis))
        acc_wallis += 1

    print(f'Wallis: num_dies = {acc_wallis} Differs by {wallis_pi}')

    # MC
    while abs(math.pi - pi_mc(acc_mc)) > tolerance:
        mc_pi = abs(math.pi - pi_mc(acc_mc))
        acc_mc += 1

    print(f'Monte Carlo: num_dies = {acc_mc} Differs by {mc_pi}')

    return (acc_arch, acc_wallis, acc_mc)

all_pi(0.1)
