#https://www.youtube.com/watch?v=nEoQq-FTMtA&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=76
#ideaStorage
import random
def storeIdea():
    f = open("ideaStorage.txt","a")
    onderwerp = input("Whats your Subject?: ")
    idea = input("Elaborate: ")
    f.write(f"{onderwerp}: {idea}\n")
    f.close()

def readIdea():
    f = open("ideaStorage.txt","r")
    contents = f.readlines()
    idea = random.choice(contents)
    print(idea)
    f.close()

while True:
    menu = input("1: StoreIdea2: printRandomIdea\n> ")
    if menu == "1":
        storeIdea()
    elif menu =="2":
       readIdea() 
    else:
        break
