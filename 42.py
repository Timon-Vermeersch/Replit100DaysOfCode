#https://www.youtube.com/watch?v=sizWhMe5Tog&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=58
#mokebeast pokedex1
pokemon = {"name":"None","Type":"None","Special Move":"None","HP":"None","MP":"None"}

def printDict():
    for name,value in pokemon.items():
        if pokemon["Type"] == "fire":
          print(f"\033[031m", end = "")
        elif pokemon["Type"] == "water":
           print(f"\033[034m", end = "") 
        elif pokemon["Type"] == "electricity":
           print(f"\033[1;33m", end = "")
          
        print(f"{name:15}:{value}")
        print("\033[0m")

for name, value in pokemon.items():
    new = input(f"What's the {name} of the pokemon?: ")
    pokemon[name] = new.strip().lower()
printDict()
