def chunked(sym, num):   # The announce a function with two parameters: a list and an int datatype
    L = list()           # Initialization a local variable in the empty list datatype
    for i in range(0, len(sym), num):   # Iteration the sym variable with the num step
        L.append(sym[i: i + num])       # Appending to the list a slice from i to i + num
    return L                            # Returning the L list
    
s = input().split()                     # Input strings with spaces and they turn into a list
n = int(input())                        # Input an int datatype to divide on chunks
print(chunked(s, n))                    # Calling up the function