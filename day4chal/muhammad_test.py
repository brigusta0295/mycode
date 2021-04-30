#!/usr/bin/env python3

ali = {"name":{"birth":"Cassius Clay","current":"Muhammad Ali"},"contact":{"phone":"333-444-5555","email":"thebest@boxing.com"},"favorites":{"number":56,"food":{"baked chicken":3.5,"mac and cheese":4.5,"spinach":2,"green peas":2},"drink":{"adult":["none"],"nonadult":["Mr. Champ soda"]}}}

# Favorite food

foodlist = ali.get('favorites').get('food').keys()
print("Muhammed Ali's Favorite foods")
for x in foodlist:
    print(x)

#Print favorit soda for number of wins

totalwins = ali.get('favorites').get('number')
drink = ali.get('favorites').get('drink').get('nonadult')

wins = 0
while wins < totalwins:
    print(drink)
    wins = wins + 1
