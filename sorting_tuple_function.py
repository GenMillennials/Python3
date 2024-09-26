athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
def sorting_name(x):
    return x[0]

def sorting_age(x):
    return x[1]

def sorting_height(x):
    return x[2]

def sorting_mass(x):
    return x[3]

dict_athletes = {1: sorting_name, 2: sorting_age, 3: sorting_height, 4: sorting_mass}

command = int(input())

m = sorted(athletes, key=dict_athletes[command])

for i in m:
    print(*i)
