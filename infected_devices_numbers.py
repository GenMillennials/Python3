# The infected devices numbers search
word = "anton"                         # The word which will being checked
for i in range(1, int(input()) + 1):   # Input amount entered words
    s = input()                        # Input each word
    result = ""                        # Initialized an empty string
    for j in word:                     # Nested loop: the sorting entered word "anton" with its consisted letters
        if j in s:                     # Search each letter in entered substring 
            result += j                # If True, the letter is adding to result variable
            s = s[s.find(j):]          # Deleting the first found letter from "s" string by its index. The entered string "s" deleting to its end for the next iteration
    if result == word:                 # If after all iterations result matchs word "anton"
        print(i, end=" ")              # the print function output the iteration number for each matching word "s" variable with space