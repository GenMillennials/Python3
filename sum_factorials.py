def fact(num):
    p=1
    for i in range(1,num+1):
        p=p*num
    return p

def sigmafact(num):
    s=0
    for i in range(1,num+1):
        s=s+fact(i) # For each number i in iterations
    return s

num=int(input())
print(sigmafact(num))