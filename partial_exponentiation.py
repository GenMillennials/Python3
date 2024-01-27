""" def genpow(n):
    return lambda a: a ** n

square = genpow(2)
cube = genpow(3)
a = float(input())
print(square(a))
print(cube(a))
n = int(input())
userpow = genpow(n)
print(userpow(a))
print(genpow(n) (a)) """


def fastpow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fastpow(a * a, n // 2)
    else:
        return fastpow(a, n-1) * a

def genpow(n):
    return lambda a: fastpow(a, n)

square = genpow(2)
cube = genpow(3)
a = float(input())
print(square(a))
print(cube(a))
n = int(input())
userpow = genpow(n)
print(userpow(a))
print(genpow(n) (a))
    