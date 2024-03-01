""" n = int(input())
char = 97 + (n - 1)
ttl = ""
for i in range(97, char + 1):
    letter = chr(i)
    ttl += letter
print(list(ttl)) """

n = int(input())
s = ""
for i in range(n):
    s += chr(ord("a") + i)
print(list(s))