#!/usr/bin/env python3

#corrected Shebang

# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.
def add(num1,num2):
    print("\n" + str(num1) + " + " + str(num2) + " = " + str(num1 + num2)) # updated \n to "\n"

def sub(num1,num2):
   print("\n" + str(num1) + " - " + str(num2) + " = " + str(num1 - num2))

def main(): # Placed : to fix syntax
    calcl = 0
    calc2 = 0
    while calc1 != "q":
        print("\nWhat is the first operator? Or, enter q to quit: ")
        calc1 = input()
        if calc1.lower() == "q":
            break
        calc1 = float(calc1)
        print("\nWhat is the second operator? Or, enter q to quit: ")
        calc2 = input(i)
        if calc2.lower() == "q":
            break
        calc2 = float(calc2)
        print("Enter an operation to perform on the two operators (+ or -): ")
        operation = input()
        if operation == "+":
            add(calc1,calc2)
        elif operation == '-': # Replaced ifel with elif
            sub(calc1,calc2)
        else:
            print("\n Not a valid entry. Restarting...")

main()
