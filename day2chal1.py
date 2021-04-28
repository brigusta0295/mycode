#!/usr/bin/env python3
heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "magic",
    "archenemy": "Voldemort",},
"captain america":
    {"real name": "Steve Rogers",
    "powers": "frisbee shield",
    "archenemy": "Hydra",}
        }

print("What character do you want to know about? Wolverine, Harry Potter, Captain America")
char_name = input(">> ")
print("What statistic do you want to know about? Real Name, Powers, Archenemy")
char_stat = input(">> ")
char_value=heroes[char_name.lower()].get(char_stat.lower(),"Stat not listed")
print(f"{char_name.title()}'s {char_stat.lower()} is: {char_value}")
