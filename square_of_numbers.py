""" L=[-2, 3, 0, 5, 7, 12, -8]
print(L)
M=[]
for el in L:
    M.append(pow(el, 2))
print(M)
 """

""" L=[-2, 3, 0, 5, 7, 12, -8]
print(L)
M=[el * el for el in L]
print(M) """

# Using the map(f, L) function
# The first argument takes a transforming function and the second takes the iterable object
# The map function transformates elements of iterable object and returns new value in the list
L=[-2, 3, 0, 5, 7, 12, -8]
print(L)
M=list(map(lambda num: num * num, L))
print(M)