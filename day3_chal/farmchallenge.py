farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# Only NE agriculture
nefarms = farms[0]['agriculture']
print("NE Farm Animals")
for animals in nefarms:
    print(animals)

choice = int(input("Choice Farm "))

for x in farms[choice]["agriculture"]:
    print(x)
