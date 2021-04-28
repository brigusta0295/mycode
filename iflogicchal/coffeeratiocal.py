#!/usr/bin/env python3
'''
Coffee calculator simulation based on the type of
brewing technique.
'''
print("Welcome to the brewing ratio calculator!")
print("Please indicate the brewing method. Chemex, Aeropress, or French Press")

while True:
    answer = input("Brewing Method? >").title()
    if answer == "Chemex":
        print("1 cup of coffee needs 30g of ground coffee and 510g water.")
        break
    elif answer == "Aeropress":
        print("1 cup of coffee needs 15g of ground coffee and 90g water.")
        break
    elif answer == "French Press":
        print("1 cup of coffee needs 30g of ground coffee and 350g water.")
        break
    else:
        print("Please select a method indicated. Chemex, Aeropress, Frech Press")
