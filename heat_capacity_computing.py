water_weight = int(input("Enter the water weight in grams "))
temp_distinction = int(input("Enter the temperature distinction in Celsius degrees "))
energy = water_weight * temp_distinction * 4.186
print(energy, "joules")
kiloWt_hour = round(energy / 3_600_000, 3)
print(kiloWt_hour, "kiloWatt in hour")
price = round(kiloWt_hour * 4.2, 3)
price_USD = round(price / 92, 4)
print(price, "rubles", end=" *** or *** ")
print(price_USD, "U.S. dollars")