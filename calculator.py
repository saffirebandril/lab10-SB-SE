#https://github.com/saffirebandril/lab10-SB-SE.git
#Partner 1: Saffire Bandril
#Partner 2: Sebastian Estrada

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or b <=0 or b==1:
        raise ValueError("Invalid logarithm input")
    return math.log(a, b)

def exponent(a, b):
    return a ** b