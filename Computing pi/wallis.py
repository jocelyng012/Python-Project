'''
CS 210 Winter 2023 Project 3
Author: Jocelyn Guan
Credit: Help hours
Description: The Wallis Method - computing pi
'''

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