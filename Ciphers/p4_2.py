'''
CS 210 Winter 2023 Project 4
Author: Jocelyn Guan
Credit: Help hours
Description: Three_rail Cipher
'''

def encrypt(msg: str) -> str:
    '''
    Take the original text and use the three-rail
    encryprtion

    >>> encrypt('There is no reason anyone would want a computer in their home.')
    Trinrs yeoda cpeitihehesoeoao u naournhro.e   annnwlwt mt  e m
    '''

    rail_1 = ''
    rail_2 = ''
    rail_3 = ''
    acc = 0

    for ch in msg:
        if acc % 3 == 0:
            rail_1 = rail_1 + ch

        elif acc % 3 == 1:
            rail_2 = rail_2 + ch

        else:
            rail_3 = rail_3 + ch

        acc += 1
    
    cipher_text = rail_1 + rail_2 + rail_3

    return cipher_text

def decrypt(msg: str) -> str:
    '''
    Decrypt the message that already encrypted and
    returning the original message

    >>> decrypt('Trinrs yeoda cpeitihehesoeoao u naournhro.e   annnwlwt mt  e m')
    There is no reason anyone would want a computer in their home.
    '''

    original = ''
    
    rail = len(msg) % 3

    rail_len = len(msg) // 3
    
    if rail == 0:
        rail_1 = msg[ :rail_len]
        rail_2 = msg[rail_len:rail_len * 2]
        rail_3 = msg[rail_len * 2: ]

    else:
        rail_1 = msg[ :rail_len + 1]
        rail_2 = msg[(rail_len + 1):((rail_len + 1) * 2)]
        rail_3 = msg[((rail_len + 1) * 2): ]

    for i in range(rail_len):
        original = original + rail_1[i]
        original = original + rail_2[i]
        original = original + rail_3[i]

    if len(rail_3) < len(rail_1):
        original = original + rail_1[-1]

    if len(rail_3) < len(rail_2):
        original = original + rail_2[-1]
    
    return original