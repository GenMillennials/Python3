# Ariphmetic progression
""" n = int(input())
L = list(range(1, n + 1))
print(L)
print(sum(L))
 """

# Geometric progression
""" n = int(input())
L = []
for i in range(n):
    L.append(2 ** i)
    print(L)
    print(sum(L)) """

# Geometric progression generator
def geometric(n, start, step):
        yield start
        for i in range(n - 1):
                start = start * step
                yield start


n = int(input())
L = [i for i in geometric(n, 1, 2)]
print(L)
print(sum(L))