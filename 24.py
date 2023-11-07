#https://www.youtube.com/watch?v=AEpcNiqV73k
import random
def diceRoll(userSides):
   doevoort = "yes"

   while doevoort == "yes":
      randomgetal= random.randint(1,int(userSides))
      print(randomgetal)

      
      doevoort = input("Type yes for one more!!")
   if doevoort != "yes":
      print("bye")

    

userSides = input("hoeveel kanten?")


diceRoll(userSides)


