# Total time in seconds calculator
d = int(input("Enter a number of days "))
h = int(input("Enter a number of hours "))
m = int(input("Enter a number of minutes "))
s = int(input("Enter a number of seconds "))
res = d * 86_400 + h * 3_600 + m * 60 + s
print("Total time in seconds is", res)