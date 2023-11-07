#https://www.youtube.com/watch?v=mn1n5db71to&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=68
clue = {}



            
def prettyPrint1():
    print()
    for key,value in clue.items():
        print(key, end = ": ")
        for subkey, subvalue in value.items():
            print(subkey,subvalue , end = " ")
        print("\t")

       

while True:
    name = input("Name?: ")
    location = input("Location?: ")
    weapon = input("Weapon?: ")

    clue[name] = {"Location": location,"weapon": weapon}
    
    prettyPrint1()


