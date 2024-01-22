""" def func(num): # параметр функции при её определении абстрактоное название для num
    p=num*2
    return p

n=4     # конкрентное название для аргумента функции
print(func(n)) # аргумент функции """


""" lambda x: x % 2 == 0
(lambda x: x % 2 == 0)(2) """

""" is_even = lambda x: x % 2 == 0 """
""" is_odd = lambda x: x % 2 != 0 """
""" is_odd(5) """


""" M = list(range(100))
filtered_numbers = list(filter(lambda n: n % 2 == 0, M))

def sqrt(num):
    return num * num

mapped_numbers = list(map(sqrt, filtered_numbers))
print(mapped_numbers) """

""" def custom_filter(func, array):
    iterator = []
    for item in array:
        result = func(item)
        if result == True:
            iterator.append(item)
    return iterator

result = custom_filter(lambda n: n % 10 == 0, M) """
""" print(result) """



import random
import names

def create_user(name: str, have_passport: bool):
    return {
        "name": name,
        "have_passport": have_passport,
    }

def get_name(): 
    return names.get_first_name()

def generate_have_passport():
    if random.random() > 0.5:
        return True
    return False

def user_fabric(f, n, p):
    return f(n(), p())

""" users = map(lambda user: user_fabric(create_user, get_name, generate_have_passport), range(10))

verified_users = list(sorted(users, key = lambda user: user["name"])) """
print(user_fabric(create_user, get_name, generate_have_passport))

