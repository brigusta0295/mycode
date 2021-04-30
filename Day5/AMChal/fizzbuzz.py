#!/usr/bin/env python3

# Fizzbuzz Challenge

r = range(1,101)

print("Printing Range 1 to 100")
for n in r:
    print(n)

print("\n Print Fizzbuzz")
for n in r:
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)

