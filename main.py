names_reestr=["Vasya", "Vadim"]

def greet_controller(names):
    for name in names:
        print(get_hello(name))
    print('\n')

def get_hello(name):
    return "Hello " + name

greet_controller(names_reestr)
greet_controller(["Vova","Dima","Sasha"])
second_array=["Slava"]
second_array.append("Fedya")
second_array.append("Andrey")

def get_any_names(any_names):
    return any_names
greet_controller(get_any_names(["Kolya", "Victor"]))
greet_controller(second_array)

def func(f):
    return f("Azaza")

print(func(get_hello))
print(func(get_any_names)) 

import random 

def sqrt(num):
    result= num*num
    return result

print(sqrt(sqrt(sqrt(5))))
print(sqrt(random.random()))