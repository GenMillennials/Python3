# The function definition
def find_all(target, symbol):
    L = list()
    for i in range(len(target)):
        if target[i] == symbol:
            L.append(i)
    return L

# input a strings to search
s = input()
char = input()

# output the result
print(find_all(s, char))