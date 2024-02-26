print ("Enter the dog name")
dog_name = input()
print ("Enter years in dog age.\nIf dog isn't a year, enter 0")
age = int(input())
if age == 0:
    print("Enter the months age of the dog")
    month = int(input())
    human_age = round(( 10 / 12) * month, 1)
elif age == 1 or age == 2:
    human_age = int(age  *10)
else:
    human_age = int((age - 2) * 7 + 20)
print(dog_name, "has age in human:", human_age)