n = int(input())
L = []
s = ""
for _ in range(n):
    L.append(input())
k = int(input())
for i in L:
    if k <= len(i):
        s += i[k - 1]
print(s)