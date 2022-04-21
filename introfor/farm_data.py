#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

def main():
    
#    for farm in farms:
#        print(farm)
#    for animal in farms[0]["agriculture"]:
#        print(animal)
#    for each_farm in farms:
#        print(each_farm["name"])
    farm_req = input("Enter a farm to request information:  ")
    for farm in farms:
        if farm["name"].lower() == farm_req.lower():
            print(farm["agriculture"])
        else:
            print("Sorry...no information for that entry.")
            break

if __name__ == "__main__":
    main()
