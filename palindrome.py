# Create a palindrome with max lenght from set of letters.
# Forbidden to crossing out the letters.
# Forbidden to getting rearranged of the letters.

def pal(S):
    if len(S)==0:
        return ""
    elif len(S)==1:
        return S
    elif (S[0]==S[-1]):
        return S[0]+pal(S[1:-1])+S[-1]
    else:
        A=pal(S[:-1])
        B=pal(S[1:])
        if len(A)>=len(B):
            return A
        else:
            return B
S=input()
print(pal(S))