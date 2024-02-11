# Miles per gallon into liters per 100 km converter

m = float(input("Input miles per gallon "))
liter_per_100km = round((3.78 / (m * 1.609)) * 100, 2)
print(f"{m} miles per gallon are {liter_per_100km} liters per 100 km")