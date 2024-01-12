""" namesReestr=["Vasya", "Vadim"]

def greetController(names):
    for name in names:
        print(getHello(name))
    print('\n')

def getHello(name):
    return "Hello " + name

greetController(namesReestr)
greetController(["Vova","Dima","Sasha"])
secondArray=["Slava"]
secondArray.append("Fedya")
secondArray.append("Andrey")

def getAnyNames(anyNames):
    return anyNames
greetController(getAnyNames(["Kolya", "Victor"]))
greetController(secondArray)

def func(f):
    return f("Azaza")


print(func(getHello))
print(func(getAnyNames)) """

import random 

def sqrt(num):
    result= num*num
    return result

print(sqrt(sqrt(sqrt(5))))
print(sqrt(random.uniform(1,100)))