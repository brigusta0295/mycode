#!/usr/bin/env python3
user_name = input("What is your name?")
weekday = input("What is the day of the week?")
print("Hello, " + user_name +"!" +" Happy " + weekday +"!")
print(f"Hello, {user_name}! Happy {weekday}!")
print("Hello, {}! Happy, {}!".format(user_name,weekday))
