# Searching the intersection two sets and the difference one yet

x1 = set(int(i) for i in input().split())
x2 = set(int(i) for i in input().split())
x3 = set(int(i) for i in input().split())
print(*sorted(x1 & x2 - x3, reverse=True))
