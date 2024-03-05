'''
CS 210 Winter 2023 Project 5
Author: Jocelyn Guan
Credit: Help hours
Description: Postfix Notation
'''

def is_operand(opreand: str) -> bool:
    '''
    reture true if opreand is an integer,
    false otherwise.

    >>> is_operand(3.5)
    False
    >>> is_operand(3)
    True
    '''
    try:
        num = int(opreand)
        result = True
    except:
        result = False

    return result

def is_operator(operator: str) -> bool:
    '''
    reture true if operator are +-*/,
    fasle otherwise

    >>> is_operator('!')
    False
    >>> is_operator('*')
    True
    '''
    vaild_operator = '+-*/'

    if operator in vaild_operator:
        return True

    else:
        return False


def apply_operator(op: str, oper_1: float, oper_2: float) -> float:
    '''
    Evaluate oper_1 and oper_2 by the op

    >>> apply_operator('*', 3, 4)
    12
    >>> apply_operator('/', 4, 2)
    2.0
    '''

    if (op == '+'):
        return (oper_1 + oper_2)
    elif (op == '-'):
        return (oper_1 - oper_2)
    elif (op == '*'):
        return (oper_1 * oper_2)
    elif (op == '/'):
        return (oper_1 / oper_2)


def eval_postfix(expr_str: str) -> float:
    '''
    Evaluate the exper_str in postfix experssion

    >>> eval_postfix('3 4 +')
    7.0
    >>> eval_postfix('3 4 + 7 *')
    49.0
    >>> eval_postfix('3 4.5 +')
    Error on postfix experssion
    '''

    stack = []
    expr_str = expr_str.split()

    for i in expr_str:
        if is_operand(i )== True:
            stack.append(int(i))
            
        elif is_operator(i):
            if len(stack) >= 2:
                op_2 = stack.pop()
                op_1 = stack.pop()

                result = apply_operator(i, float(op_1), float(op_2))
                stack.append(result)
            else:
                return "error on postfix expression"
        else:
            return "error on postfix expression"
            
    if len(stack) == 1:
        return stack[0]
    else:
        return "error on postfix expression"

# how to add a error message
#ask lab xlsl (predict value (yes or no))
'''
eval_postfix('3 3 4 + 7 * /')
eval_postfix('3 4 +')
eval_postfix('3 4 + 7 *')
'''
#print(apply_operator('-', 1.0, 2.0))
#print(eval_postfix('49 3.5 4 + 7 * /'))
#print(eval_postfix('3 4 - 7 *'))
print(eval_postfix('3 4 ++'))
