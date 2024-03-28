left = {'(':')', '[':']', '{':'}', '<':'>'}
right = set(left.values())
s = "(k * [f + g * (a + b) * d + e) * k + l] + h * (<i> + j)) * {m + n}"
stack = []
flag = True
for i in range(len(s)):
    if s[i] in left:
        stack.append(s[i])
    elif s[i] in right:
        if len(stack) == 0 or s[i] != left[stack.pop()]:
            f = False
            break
if len(stack) > 0:
    f = False
print(f)