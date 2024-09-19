def mean(*args):
    L = [i for i in args if type(i) in (int, float)]
    if len(L) == 0:
        return 0.0
    return sum(L) / len(L)

print(mean(2, [58, 'Yes'], 84, -5, 'no', (2, 45), 3))