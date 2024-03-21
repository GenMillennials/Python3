t = [int(el) for el in input().split()]
print(t)
T = [[t[0]]]
for i in range(1, len(t)):
    if t[i] > t[i-1]:
        T[-1].append(t[i])
    else:
        T.append([t[i]])
print(T)
m = max(len(p) for p in T)
print(m)
T1 = [p for p in T if len(p) == m]
print(T1)
d = max([p[-1] - p[0] for p in T1])
print(d)