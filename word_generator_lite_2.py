# Generated words may be mindless but they should consist of letters used once in the word.
# If the lenght a word equals all letters in the alphabet, the amount of possible words match counting of all 
# permutations in the alphabet.

""" The first code version (without a library)

def permutation(alph,rep):
    L=[]
    if rep==1:
        for i in alph:
            L.append(i)
    else:
        for a in alph:
            beth=alph.replace(a,"")
            for p in permutation(beth,rep-1):
                L.append(a+p)
    return L

for p in permutation("abc",3):
    print(p) """

# The second code version with standard Python's library itertools

from itertools import permutations  # Calling the product function from intertools

P=list(permutations("abc")) # Combinations iterating process and returning the list
for p in P:
    print("".join(p)) # Merging the list elements content into one element