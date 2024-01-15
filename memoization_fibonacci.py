F=[]          # Create a global list for the Fibonacci sequence storing
def fib(num):
    global F  # Definition a global variable inside for changing the global list F[] by the def fib(num)
    if num>=len(F): 
          F=F+[-1]*(num+1)  # Add the memory if lenght F[] shorter than current stack
    if F[num]==-1:  # Checking calculated numbers early (the memoization process)
        if num<=2:
            F[num]=1 # Working out terminal cases if num==1 or num==2
        else:
            F[num]=fib(num-1)+fib(num-2) # Calculation the Fibonacci sequence through recursion
    return F[num]

num=int(input())
print(fib(num))