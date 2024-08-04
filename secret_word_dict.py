s = input()
my_dict = {}

for _ in range(int(input())):
    value, key = input().split(": ")
    my_dict[int(key)] = value
    
for symb in s:
    print(my_dict[s.count(symb)], end="")
