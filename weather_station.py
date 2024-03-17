n = int(input())
cntr = 1
m = 0    # The day amount with increasing temperature
for i in range(n):
    t = int(input())
    if i > 0:
        if t > t1:
            cntr += 1
            if m < cntr:
                m = cntr
        else:
            cntr = 1
    t1 = t    # Saving temperature in the previous day in the loop
print(m)