#!/usr/bin/env python3
'''
Coffee calculator simulation based on the type of
brewing technique.
'''
print("Welcome to the brewing ratio calculator!")
print("Please indicate the brewing method. Chemex, Aeropress, or French Press")

coffeedict= {
        "Chemex": "1 cup of coffee needs 30g of ground coffee and 510g water.",
        "Aeropress": "1 cup of coffee needs 15g of ground coffee and 90g water.",
        "French Press": "1 cup of coffee needs 30g of ground coffee and 350g water."
        }

def coffee(answer):
    if answer in coffeedict.keys():
        print(coffeedict[answer])
                
while True:

    answer = input("Brewing Method? >").title()

    coffee(answer)
    
    cont = input("Would you like to brew another technique? Y or N ").upper()
    if cont == "Y":
            answer = ""
    elif cont == "N":
            break
    else:
            break
