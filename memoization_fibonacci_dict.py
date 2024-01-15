V={}    # Create an empty dictionary for the Fibonacci sequence storing
def fib(num):
    if num not in V:  # Checking numbers in the outer dictionary (the memoization process)
        if num<=2:  # Working out terminal cases if num==1 or num==2
            V[num]=1
        else:
            V[num]=fib(num-2)+fib(num-1)  # Calculation the Fibonacci sequence through recursion
    return V[num]

num=int(input())
print(fib(num))