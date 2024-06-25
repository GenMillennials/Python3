# Checking the same number in two sets

s1, s2 = set(input()), set(input())
if s1.isdisjoint(s2):
    print("NO")
else:
    print("YES")
