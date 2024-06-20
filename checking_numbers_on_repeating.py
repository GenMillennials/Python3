# Checking numbers on repeating

num = [int(i) for i in input().split()]
my_set = set()
for i in range(len(num)):
    if num[i] in my_set:
        print("YES")
    else:
        print("NO")
        my_set.add(num[i])
