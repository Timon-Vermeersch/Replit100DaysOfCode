class Character:
    name : str
    health = 100
    magicPoints = 50

    def __init__(self,name):
        self.name = name
        
    def printSelf(self):
        print(f"Character {self.name} has {self.health}HP and {self.magicPoints}MP\n")
    
    def setStats(self,health,magicPoints):
        self.health = health
        self.magicPoints = magicPoints

class Player(Character):
    nickName: str
    lives =  3

    def __init__(self,nickName):
        self.name = "Player"
        self.nickName = nickName

    def printSelf(self):
        print(f"Character {self.name} or {self.nickName} has {self.health}HP and {self.magicPoints}MP and {self.lives} lives\n")
    def isAlive(self):
        if self.lives > 0:
            print(f"{self.nickName} is Alive!")
            return True
        else:
            print(f"Rest in pieces {self.nickName}")
            return False

class Enemy(Character):
    type : str
    strenght : int

    def __init__(self,name,type,strenght):
        self.name = name
        self.type = type
        self.strenght = strenght

class Vampire(Enemy):

    day : bool

    def __init__(self,day):
    
        self.name = "Vampire"
        self.type = "Vampire"
        self.strenght = 100
        self.day = day

    def printSelf(self):
        print(f"{self.name} has {self.health}HP {self.magicPoints}MP {self.strenght} strenght and day is: {self.day}")

class Orc(Enemy):
    speed = int

    def __init__(self,speed):
        self.name = "Orc"
        self.type = "Orc"
        self.strenght = 200
        self.speed = speed

    def printSelf(self):
        print(f"{self.name} has {self.health}HP {self.magicPoints}MP {self.strenght} strenght and {self.speed} speed")





if  __name__ == "__main__":

    geertje = Character("Geertje")
    geertje.printSelf()


    ian = Player("Ian the mighty")
    
    sharry = Orc(250)

    shallo = Orc(300)

    shooker = Orc(220)

    nomit = Vampire(True)


    sharry.printSelf()
    shallo.printSelf()
    shooker.printSelf()
    nomit.printSelf()
    ian.printSelf()
    ian.isAlive()
    
    



