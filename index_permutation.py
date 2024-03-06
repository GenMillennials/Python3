L = input().split()
L2 = list()
for i in L:
    L2.append(int(i))
L_max = max(L2)
L_min = min(L2)
L_max_index = L2.index(L_max)
L_min_index = L2.index(L_min)
L2[L_max_index], L2[L_min_index] = L2[L_min_index], L2[L_max_index]
print(*L2)