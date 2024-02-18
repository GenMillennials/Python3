""" # Total time in seconds calculator
d = int(input("Enter a number of days "))
h = int(input("Enter a number of hours "))
m = int(input("Enter a number of minutes "))
s = int(input("Enter a number of seconds "))
res = d * 86_400 + h * 3_600 + m * 60 + s
print("Total time in seconds is", res) """

# Time converter
sec_per_d = 86_400
sec_per_h = 3_600
sec_per_m = 60
sec_per_s = 1
sec = int(input("Enter the total time in seconds "))
days = sec // sec_per_d
sec = sec % sec_per_d
hours = sec // sec_per_h
sec = sec % sec_per_h
minutes = sec // sec_per_m
sec = sec % sec_per_m
seconds = sec
print(f"{days} d : {hours:02} h : {minutes:02} m : {seconds:02} s")