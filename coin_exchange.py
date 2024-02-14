# Coin exchange
cents_per_toonie = 200
cents_per_loonie = 100
cents_per_quarter = 25
cents_per_dime = 10
cents_per_nickel = 5
cents = int(input("Enter the amount in cents: "))
print(" ", cents // cents_per_toonie, "two dollar coins")
cents = cents % cents_per_toonie
print(" ", cents // cents_per_loonie, "one dollar coins")
cents = cents % cents_per_loonie
print(" ", cents // cents_per_quarter, "quarter coins")
cents = cents % cents_per_quarter
print(" ", cents // cents_per_dime, "dime coins")
cents = cents % cents_per_dime
print(" ", cents // cents_per_nickel, "nickel coins")
cents = cents % cents_per_nickel
print(" ", cents, "cents")