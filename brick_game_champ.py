n = int(input())
V = {}
for i in range(n):
    s = input().split()
    name = s[0]
    score = int(s[1])
    V[name] = score
print(V)