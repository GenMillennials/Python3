# The general formula is v = sqrt(v_init**2 + 2 * a * gravity)
# v_init = 0
# The general formula falling time is sqrt(2 * d / gravity)
# gravity = 9.8 meters per squared second
from math import sqrt
gravity = 9.8
d = float(input("Enter the falling distance "))
v = round(sqrt((2 * gravity * d)), 2)
falling_time = round(sqrt(2 * d / gravity), 2)
print("The free fall velocity is", v, "meters per second at the ground")
print("The falling time is", falling_time, "seconds")