#https://www.youtube.com/watch?v=2XBhtE3Pl6M&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=48
names = []
def askName():
   voornaam =  input("wat is uw voornaam: ").strip().capitalize()
   achternaam = input("wat is uw achternaam: ").strip().capitalize()
   return voornaam, achternaam
def addTuple():
   names.append((voornaam,achternaam)) 
def printTuple():
   print(f"Voornaam: {voornaam} Achternaam: {achternaam}")
def print_t():
  for i in range(0,len(names)):
    print(f"Name {i + 1}: {names[i][0]} {names[i][1]}")

while True:
   voornaam, achternaam = askName()

   if voornaam == "":
    for (voornaam, achternaam) in names: 
     printTuple() 
     print_t()
   elif (voornaam, achternaam) in names:
     print("already present")
   elif (voornaam, achternaam) not in names:
     addTuple()


      
