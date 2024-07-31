s1 = sorted([i for i in input().lower() if i.isalpha()])
s2 = sorted([i for i in input().lower() if i.isalpha()])

dict1 = dict(zip(range(len(s1)), s1))
dict2 = dict(zip(range(len(s2)), s2))

if dict1 == dict2:
    print("YES")
else:
    print("NO")
