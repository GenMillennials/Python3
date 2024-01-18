# Create a palindrome with max lenght from set of letters.
# Forbidden to crossing out the letters.
# Forbidden to getting rearranged of the letters.

def pal(S,left,right):  # Definition a function with 3 parameters: string, left and right substrings
    if left==right:  # The first terminal case if the string consist of one letter
        return S[left]
    elif left==right-1:  # The second terminal case if matching the letter of left substring to the previous letter of the right substring
        if S[left]==S[right]:  # If they equal, 
            return S[left]+S[right]  # returning both letters, 
        else:
            return S[left]  # unlike return the left letter only
    elif (S[left]==S[right]): # If left and right letters equal,
        return S[left]+pal(S,left+1,right-1)+S[right] # returning the recursion function and add the result to left and to right
    else:  
        A=pal(S,left,right-1) # Recursion for two functions to compare lenghts both substrings and returning one more lenght
        B=pal(S,left+1,right)
        if len(A)>=len(B):
            return A
        else:
            return B
        
S=input()
print(pal(S,0,len(S)-1))