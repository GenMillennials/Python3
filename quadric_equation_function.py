# Solving the quadric equation with obligatory two roots
from math import sqrt

def solve(a, b, c):
    x1, x2 = 0, 0
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
    elif D == 0:
        x1 = -b / (2 * a)
        x2 = -b / (2 * a)  # for right output in the task
    return min(x1, x2), max(x1, x2)

a, b, c = int(input()), int(input()), int(input())

x1, x2 = solve(a, b, c)  # Extraction of the value at the output function
print(x1, x2)