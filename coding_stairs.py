n = int(input())   # Input the levels amount in a stair
L = [n] + [0] * (n - 1)   # n is the higher level and (n-1) is the step amount on the stair
print(L)   # The stair starting condition
M = [L]    # Creatind another list for storing possible step combinations
for L in M:   # The start of loop inside "M" list
    for i in range(len(L)):   # Iteration on each index in "L" list
        if L[i] > 2:          # Checking condition on more 2, for passing to the inner loop
            for j in range(i + 1, len(L)):   # Another loop for start iteration and won't out of range
                L1 = copy(L)                 # Copying the "L" list to keep it
                L1[i] = L1[i] - 1            # Decreasing current value on 1
                L1[j] = L1[j] + 1            # Increasing current value on 1 in the next program step