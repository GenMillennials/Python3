words = {}
for i in range(int(input())):
    a, b = input().split()
    words[a], words[b] = b, a
print(words[input()])
