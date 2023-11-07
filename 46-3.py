
pokeDex = {}
#---------------------------------------------
def printPokemon():
    for name,value in pokemon.items():
        if pokemon["Type"] == "fire":
          print(f"\033[031m", end = "")
        elif pokemon["Type"] == "water":
           print(f"\033[034m", end = "") 
        elif pokemon["Type"] == "electricity":
           print(f"\033[1;33m", end = "")
          
        print(f"{name:^15}:{value}")
        print("\033[0m")
#---------------------------------------------
def printPokedex():
   print(f'{"Name":^15} | {"Type":^15} | {"Special":^15} | {"HP":^15} | {"MP":^15}')
   for value in pokeDex.values():
      for index,subvalue in enumerate(value.values()):
         if index == len(value.values())-1:
            print(f'{subvalue:^15}', end = "  ")
         else:
            print(f'{subvalue:^15}', end = " | ")
      
      print("")
#---------------------------------------------
def createPokemon():
   pokemon = {"name":"None","Type":"None","Special Move":"None","HP":"None","MP":"None"}
   for key in pokemon.keys():
    new = input(f"What's the {key} of the pokemon?: ")
    pokemon[key] = new.strip().lower()
 
   return pokemon
 #---------------------------------------------   
#---------------------------------------------
def savePokemon(pokemon):
   pokemonName = pokemon["name"]
   print(pokemonName)
   pokeDex[pokemonName] = pokemon
   
 #---------------------------------------------  
#---------------------------------------------
while True:
    newPokemon = createPokemon()
    savePokemon(newPokemon)
    printPokedex()

