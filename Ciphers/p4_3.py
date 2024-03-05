'''
CS 210 Winter 2023 Project 4
Author: Jocelyn Guan
Credit: Help hours
Description: ROT- 13 Cipher
'''

def encrypt(msg: str) -> str:
    '''
    Encrypt the message by using the ROT-13

    >>> enctypt('Two driven jocks help fax my big quiz')
    gjb qevira wbpxf uryc snk zl ovt dhvm
    '''

    low_case= msg.lower()

    new_text = ''

    text_1 = 'abcdefghijklmnopqrstuvwxyz '
    text_2 = 'nopqrstuvwxyzabcdefghijklm '
    

    for ch in low_case:
        index_ch = text_1.find(ch)
        new_ch = text_2[index_ch]

        if ch not in text_1 and text_2:
            new_ch = ch

        new_text = new_text + new_ch

    return new_text

def decrypt(msg: str) -> str:
    '''
    Decrypt the message that already encrypted and
    returning the original message

    >>> decrypt('gjb qevira wbpxf uryc snk zl ovt dhvm')
    Two driven jocks help fax my big quiz
    '''

    new_text = ''

    text_1 = 'abcdefghijklmnopqrstuvwxyz '
    text_2 = 'nopqrstuvwxyzabcdefghijklm '

    for ch in msg:
        index_ch = text_2.find(ch)
        new_ch = text_1[index_ch]

        if ch not in text_1 and text_2:
            new_ch = ch

        new_text = new_text + new_ch

    return new_text