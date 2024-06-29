# Scores one in three pupils

x1 = set(int(i) for i in input().split())
x2 = set(int(i) for i in input().split())
x3 = set(int(i) for i in input().split())

print(*sorted((x3 - x2 - x1), reverse=True))   # Difference two set values from third pupils