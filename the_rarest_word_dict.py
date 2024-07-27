L = input().lower().split()
x = [i.strip(".,!?:;-") for i in L]
dict1 = {}

for i in x:
    dict1[i] = x.count(i)

res = {}
min_count = min(dict1.values())

for key, value in dict1.items():
    if value == min_count:
        res[key] = value 
print(min(res))