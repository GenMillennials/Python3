from math import pi

r = float(input("Enter the radius for a circle and ball "))
S = round(pi * r ** 2, 3)
print("Circle area is", S)
V = round((4 / 3) * pi * r ** 3, 3)
print("Ball volume is", V)