import math

def add(a,b):
    return a + b


def subtraction(a,b):
    return a - b


def multiplication(a,b):
    return a * b


def quotient(a,b):
    return a / b

def remains(a,b):
    return a % b


def log_10(a):
    return math.log10(a)


def exponentiation(a,b):
    return a ** b


a = int(input("Input a "))
b = int(input("Input b "))
print(add(a,b))
print(subtraction(a,b))
print(multiplication(a,b))
print(quotient(a,b))
print(remains(a,b))
print(log_10(a))
print(exponentiation(a,b))