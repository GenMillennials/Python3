print("Enter length and width the hole")
a, b = int(input()), int(input())
L = sorted([a, b])
print(L)
print("Enter length, width, and high the hole")
x, y, z = int(input()), int(input()), int(input())
M = sorted([x,y,z])
print(M)
if M[0] <= L[0] and M[1] <= L[1]:
    print("Brick will come in the wall.")
else:
    print("Brick won't come in the wall.")