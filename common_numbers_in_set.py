# The common numbers

n = int(input())
dig = [set(input()) for i in range(n)]
myset = dig[0]
for i in range(1, len(dig)):
    myset.intersection_update(dig[i])
print(*sorted(myset))
