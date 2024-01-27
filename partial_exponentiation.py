def genpow(n):
    return lambda a: a ** n

square = genpow(2)
cube = genpow(3)
a = float(input())
print(square(a))
print(cube(a))
n = int(input())
userpow = genpow(n)
print(userpow(a))
print(genpow(n) (a))