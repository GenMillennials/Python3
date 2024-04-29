S = [int (i) for i in input().split()]   # Transform str() into int() within list compehension
cntr = 0   # the counter on null
for j in range(1, len(S)):   # The For loop from 1 to lenght S list
    if S[j] > S[j - 1]:   # The If condition with comparison S[j] el and previous S[j-1] el
        cntr += 1   # if condition == True, counter increase on 1
print(cntr)   # display the counter 