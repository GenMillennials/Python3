""" n = int(input())
L = []
s = ""
for _ in range(n):
    L.append(input())
k = int(input())
for i in L:
    if k <= len(i):
        s += i[k - 1]
print(s) """

n = int(input())
L = []
for _ in range(n):
    L.append(input())
k = int(input())
res = ""
for i in range(n):
    if len(L[i]) < k:
        continue
    res += L[i][k-1]
print(res)