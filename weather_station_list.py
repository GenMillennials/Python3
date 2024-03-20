t = [int(el) for el in input().split()]
print(t)
T = [[t[0]]]
for i in range(1, len(t)):
    if t[i] > t[i-1]:
        T[-1].append(t[i])
    else:
        T.append([t[i]])
print(T)