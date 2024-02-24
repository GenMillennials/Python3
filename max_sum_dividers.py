a = int(input()) 
b = int(input())
cntr = 0
largest = 0
max_ttl = 0
for i in range(a, b + 1):
    ttl = 0
    for j in range(1, i + 1):
        if i % j == 0:
            ttl += j
        if ttl >= cntr and i >= largest:
            cntr = ttl
            largest = i
            max_ttl = ttl
print(largest, max_ttl)