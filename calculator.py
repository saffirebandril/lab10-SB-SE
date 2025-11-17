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
    return a / b

def logarithm(a, b):
    if a <= 0 or b <= 0 or b ==1:
        raise ValueError("Invalid logarithm input")
    return math.log(a, b)

def exponent(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take sqrt of negative number")
    return math.sqrt(a)