# Function definition
def merge(list1, list2):
    L = list1 + list2
    L.sort()
    return L

# Input two lists
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# Calling the function
print(merge(numbers1, numbers2))