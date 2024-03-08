print("Enter length and width the hole")
a, b = int(input()), int(input())
a, b = min(a, b), max(a, b)
print(a,b)
print("Enter length, width, and high the hole")
x, y, z = int(input()), int(input()), int(input())
x, y = min(x, y), max(x, y)
y, z = min(y, z), max(y, z)
x, y = min(x, y), max(x, y)
print(x, y, z)
if x <= a and y <= b:
    print("Brick will come in the wall.")
else:
    print("Brick won't come in the wall.")