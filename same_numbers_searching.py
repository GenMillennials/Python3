# The same numbers searching
set1 = set(int(i) for i in input().split())   # Enter the first set of numbers
set2 = set(int(i) for i in input().split())   # Enter the second set of numbers
print(*sorted(set1 & set2))                   # Checking and unification the both sets and unpacking the result
