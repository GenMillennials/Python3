from math import sqrt
a = float(input("Enter the a argument greater than null "))
b = float(input("Enter the b argument "))
c = float(input("Enter the c argument "))
D = b ** 2 - 4 * a * c
if D > 0:
    x1, x2 = 0, 0
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print(min(x1, x2), max(x1, x2), sep="\n")
elif D == 0:
    x1 = 0
    x1 = -b / (2 * a)
    print(x1)
elif D < 0:
    print("No solution")