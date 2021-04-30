#!/usr/bin/env python3

c = 0

phonebook = {}

while c < 3:
    name = input("Contacts Name: ")
    phone= input("Phone Number: ") 
    phonebook[name] = phone
    c = c + 1
print(phonebook)

for users in phonebook:
    print(users)
