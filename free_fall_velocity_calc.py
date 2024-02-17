# The formula is v = (v_init**2 + 2 * a * d) ** 0.5
# a = 9.8 meters per squared second
v_init = float(input("Enter the initial velocity "))
a = 9.8
d = float(input("Enter the falling distance "))
v = round(((v_init ** 2) + (2 * a * d)) ** 0.5, 2)
print("The free fall velocity is", v, "meters per second at the ground")