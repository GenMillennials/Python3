def check_el_amount(L):   # A function declaration with 1 parameter
    f = True              # Flag on True by defalt in "f" variable
    for i in range(1, len(L)):   # The loop initialization to iterate list "L" indices starting the second index
        if L[i] >= L[i -1]:      # Checking if the current index has more or equal value than the previous index
            f = False            # If it's true, "f" variable changes on False value
            break                # Interrupt the loop execution
        if L[i] == 0:            # Checking if the current index equals 0
            if len(set(L[i:])) > 1:   # If it's true, checking consistance the unique elements more in "L[i:]" sublist
                f = False        # If it's true, "f" variable changes on False value
            break                # Interrupt the loop execution
    return f                     # Returning the "f" value in bool datatype, True of False

n = int(input())   # Input the levels amount in a stair
L = [n] + [0] * (n - 1)   # n is the higher level and (n-1) is the step amount on the stair
print(L)   # The stair starting condition
M = [L]    # Creatind another list for storing possible step combinations
for L in M:   # The start of loop inside "M" list
    for i in range(len(L)):   # Iteration on each index in "L" list
        if L[i] > 2:          # Checking condition on more 2, for passing to the inner loop
            for j in range(i + 1, len(L)):   # Another loop for start iteration and won't out of range
                L1 = copy(L)                 # Copying the "L" list to keep it (in "light" copy)
                L1[i] = L1[i] - 1            # Decreasing current value on 1
                L1[j] = L1[j] + 1            # Increasing current value on 1 in the next program step