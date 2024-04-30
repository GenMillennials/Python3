first_q = 0
second_q = 0
third_q = 0
fourth_q = 0   # Lines 1-4 from the scratch
for i in range(int(input())):   # Create the loop with the total options amount
    L = input().split()         # Input coordinates on the list in strings data type
    if int(L[0]) > 0:           # The If condition on the X axis more null
        if int(L[1]) > 0:
            first_q += 1
        elif int(L[1]) < 0:
            fourth_q += 1
    elif int(L[0]) < 0:         # The If condition on the X axis less null
        if int(L[1]) > 0:
            second_q += 1
        elif int(L[1]) < 0:
            third_q += 1    
print(f"The First Quarter: {first_q}")
print(f"The Second Quarter: {second_q}")
print(f"The Third Quarter: {third_q}")
print(f"The Fourth Quarter: {fourth_q}")