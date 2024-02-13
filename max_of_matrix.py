# Python cannot compare lists by default.
# At first, it needs to find maximum for each row.

n=3
M=[[int(el) for el in input().split()] for i in range(n)]
for el in M:
    print(el)
L=[]
for el in M:
    L.append(max(el))
print(max(L))