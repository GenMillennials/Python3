def factorial(num1):
    counter=1
    for index in range(1,num1+1):
        counter=counter*index
    return counter

def find_arrange(num2,num1):
    return factorial(num2)//factorial(num2-num1)

def find_permutation(num1):
    return find_arrange(num1,num1)

def find_combination(num2,num1):
    return find_arrange(num2,num1)//find_permutation(num1)

num2=int(input())
num1=int(input())
print(find_combination(num2,num1))