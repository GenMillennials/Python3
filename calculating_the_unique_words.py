s = input().lower().split()   # Input the text
for i in range(len(s)):       # Iterate on the lenght of the string
    s[i] = s[i].strip(".,;:-?!")   # Clear signs in the text

set_word = set(s)   # Creation the veriable with a set that consists on unique words from the text

print(len(set_word))   # Output the unique words amount
