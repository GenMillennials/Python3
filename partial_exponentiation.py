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




""" def fastpow(a, n):
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
print(genpow(n) (a)) """




""" def fastpow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fastpow(a * a, n // 2)
    else:
        return fastpow(a, n-1) * a
    

def get_partapply(n, f):
    return lambda a: f(a, n)


square = get_partapply(2, fastpow)
cube = get_partapply(3, fastpow)
a = float(input())
print(square(a))
print(cube(a))
n = int(input())
userpow = get_partapply(n, fastpow)
print(userpow(a))
print(get_partapply(n, fastpow) (a)) """



from functools import partial


def fastpow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fastpow(a * a, n // 2)
    else:
        return fastpow(a, n - 1) * a


square = partial(fastpow, n = 2)
cube = partial(fastpow, n = 3)
a = float(input())
print(square(a))
print(cube(a))