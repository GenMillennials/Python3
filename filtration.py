# Make filtering a list where its elements more than zero

"""L=[-2,3,0,-5,7,] # Solving with structured style of programming
print(L)
M=[]
for el in L:
    if el>0:
        M.append(el)
print(M)""" 

"""L=[-2,3,0,-5,7] # Solving with the Python's style programming
print(L)
M=[el for el in L if el>0]
print(M)"""

# Soolving with the filter(f,L) embedded function
def check_positive(num): # Definition a function which checking up a number on positive or negative
    if num>0:
        return True # The function returns True or False (It's nessesary for embedded filter function)
    else:
        return False
    
L=[-2,3,0,-5,7]
print(L)
M=list(filter(check_positive,L)) # Using the filter function that delete wasted numbers in L[] list
print(M)