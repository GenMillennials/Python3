# No pupils' scores in the set

x1 = set(int(i) for i in input().split())
x2 = set(int(i) for i in input().split())
x3 = set(int(i) for i in input().split())
scores_set = set(range(11))

print(*sorted((scores_set - x1 - x2 - x3), reverse=False))
