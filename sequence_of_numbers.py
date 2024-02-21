# The sequence of numbers
""" m = int(input())
n = int(input())
if m < n:
    for i in range(m, n+1):
        print(i)
elif m > n:
    for i in range(m, n-1, -1):
        print(i)
elif m == n:
    print(m)
 """

# The sequence of odd numbers and m < n
m = int(input())
n = int(input())
start = ((m - 1) // 2) * 2 + 1  # Checking and bringing to odd number
for i in range(start, n - 1, -2):
    print(i)