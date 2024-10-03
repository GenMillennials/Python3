# The cities game for checking the duplicate early

s = [input() for i in range(int(input()) + 1)]
if len(s) == len(set(s)):
    print("OK")
else:
    print("REPEAT")
