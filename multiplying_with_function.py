""" L = [1, 4, -5, 9, 14, -8, 3] 
print(L)
p = 1
for el in L:
    p = p * el
print(p) """

from functools import reduce  # Import the reduce function from the functools Python library

L = [1, 4, -5, 9, 14, -8, 3]
print(L)
p = reduce(lambda num1, num2: num1 * num2, L)  # Using the reduce function which accumulate list values and returning a number not a list
print(p)