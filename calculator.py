# https://github.com/HanumanMonk/lab11-PR-GM.git
# Partner 1: Phu Reed
# Partner 2: Grant Martin

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

# First example
def square_root(a):
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a*b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return a/b

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    else:
        return math.log(a, b)


def exponent(a, b):
    return a**b

def mul (a, b):
    return a*b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return a/b

def exp(a,b):
    return a**b
