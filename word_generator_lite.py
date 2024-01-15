def prod(alph,rep): # Definition the function with two parameters: set of letters, and length of result
    L=[]   # Empty list is created for storing results
    if rep==1:  # Terminal cases working out, when input in "rep" argument one letter only
        for i in alph:
            L.append(i)
    else:
        for a in alph: # Creating the first letter for further merging 
            for p in prod(alph,rep-1): # Recursion for creating sets of other letters exept for the first one
                L.append(a+p) # Merging letters into list L[]
    return L # Returning L into def prod(alph,rep)

for p in prod("abc",4): 
    print(p)  # Output elements from the list L[] as a result