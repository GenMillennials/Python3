n = int(input())
V = {}
T = {}
for i in range(n):
    s = input().split()
    name = s[0]
    score = int(s[1])
    V[name] = score
    if name not in V or V[name] < score:
        V[name] = score
        T[name] = i
print(V)
print(T)
m = max(list(V.values()))
T1 = {}
for name in V:
    if V[name] == m:
        T1[name] = T[name]
print(T1)
t = min(list(T1.values()))
for name in T1:
    if T1[name] == t:
        print(name)