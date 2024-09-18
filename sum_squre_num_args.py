def sq_sum(*args):
    n = [i**2 for i in args]
    return sum(n)

print(sq_sum(2, 3, 5))