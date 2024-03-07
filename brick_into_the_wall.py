print("Enter length and width the hole")
a, b = int(input()), int(input())
print("Enter length, width and high the brick")
x, y, z = int(input()), int(input()), int(input())
if (x <= a and y <= b or y <= a and x <= b or
    x <= a and z <= b or z <= a and x <= b or
    z <= a and y <= b or y <= a and z <= b):
    print("Brick will come in the wall.")
else:
    print("Brick won't come in the wall.")