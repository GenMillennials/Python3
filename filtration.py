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

# Solving with the filter(f,L) embedded function and lambda anonymous function

L=[-2,3,0,-5,7]
print(L)
M=list(filter(lambda num: num>0, L)) # Definition lambda function as argument for True
print(M)