# Substrings in the list output
s = input().split()   # Input a string and turn it into a list
lst = []              # Creating anoter list as a temporary storage
res = [[]]            # Creating third list to accumulate a result
for i in range(len(s)):        # Initialization the first loop to iterate s list elements as an external loop
    for j in range(len(s)):    # Initialization the same loop to double iterate that list elements for generate all exist substirngs
        lst = s[j: i + j + 1]  # Generation substrings to include each element s from j to j + i + 1, if that's no out of range
        if len(lst) == i + 1:  # Filtration substirngs if length temporary storage consists on i + 1 elements in length -->
            res.append(lst)    # --> Including that string into result list
print(res)                     # Result list output in the embedded print function