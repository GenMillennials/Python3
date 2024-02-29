n = int(input())
s = input()
for i in range(len(s)):
    decr = ord(s[i]) - n
    if decr < 97:
        decr += 26
    print(chr(decr), end="")