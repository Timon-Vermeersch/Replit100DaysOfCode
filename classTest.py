class Squirtle:
    name : str
    elementType =  "water"
    trainer = None
    pokeball = None
    isInPcBox : bool
    level = 5


    def __init__(self,trainer,pokeball,isInPcBox,name = "squirtle" ):
        self.name = name
        self.trainer = trainer
        self.pokeball = pokeball
        self.isInPcBox = isInPcBox

        print(f"{self.name} caught with {self.pokeball}")

    def training(self):
        if self.level <100:
            self.level +=1

            self.checkEvolveAt2() 
    def checkEvolveAt2(self):
        if self.level == 2:
            print("OMG ITS EVOLVING")

class Wartortle(Squirtle):
    level = 16
    

    def __init__(self,move,squirtle,name = "wartortle"):
        if squirtle.name == "squirtle":
            self.name = name
        else:
            self.name = squirtle.name
        self.move = move
        self.trainer = squirtle.trainer
        self.pokeball = squirtle.pokeball
        self.isInPcBox = squirtle.isInPcBox
    def printMove(self):
        print(f"{self.name} Learned {self.move}")
        
            

squirtle1 = Squirtle("Fre", "Luxury", False, "FreIsDeBeste")
squirtle2 = Wartortle("Dickpunch", squirtle1 , "Timon" )

squirtle2.printMove()
print(squirtle2.name)
