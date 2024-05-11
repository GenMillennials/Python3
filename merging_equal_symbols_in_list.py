# The searching and aggregating the same string datatype symbols in a nested list
s = input().split()   # Input the string and turn it into the list datatype
L = [[s[0]]]          # Initialization a list with the first element on the 0 index
for i in range(1, len(s)):   # Creating a loop to iterate the other s elements for other than 0 index
    if s[i] == s[i - 1]:     # If current indice equals the previous indice -->
        L[-1].append(s[i])   # --> Addind the element into the end of the current list L
    else:                    
        L.append([s[i]])     # --> Else adding the element into the list
print(L)                     # Output the L list 