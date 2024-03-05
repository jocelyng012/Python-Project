'''
CS 210 Winter 2023 Project 4
Author: Jocelyn Guan
Credit: Help hours
Description: Simple Transposition Cipher
'''

def encrypt(msg: str) -> str:
    '''
    Cipher divides the original message into two strings
    corresponding to its even and odd characters

    >>> encrypt('It was a dark and stormy night')
    twsadr n tryngtI a  akadsom ih
    '''

    odd_chars = ''
    even_chars = ''
    char_count = 0

    for ch in msg:
        if char_count % 2 == 1:
            odd_chars = odd_chars + ch
        
        else:
            even_chars = even_chars + ch
        
        char_count += 1
    
    cipher_text = odd_chars + even_chars

    return cipher_text

def decrypt(msg: str) -> str:
    '''
    Decrypt the message that already encrypted and
    returning the original message
if
    >>> decrypt('twsadr n tryngtI a  akadsom ih')
    It was a dark and stormy night
    '''

    half_len = len(msg) // 2
    odd_chars = msg[half_len: ]
    even_chars = msg[ :half_len]
    original = ''

    for i in range(half_len):
        original = original + odd_chars[i]
        original = original + even_chars[i]

    if len(even_chars) < len(odd_chars):
        original = original + odd_chars[-1]

    return original
