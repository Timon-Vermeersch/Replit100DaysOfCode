#https://www.youtube.com/watch?v=jCtk6DZLHoQ&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=30
import random

 

def rollHealth():
    d6 = random.randint(1,6)
    d8 = random.randint(1,8)
    hp = (d6*d8)/2 + 12
    return hp

def rollStrenght():
    d6 = random.randint(1,6)
    d12 = random.randint(1,12)
    str = (d6*d12)/2 + 10 
    return str


def createChar():

    uname = input("enter char name: ")
    hp = rollHealth()
    str = rollStrenght()
    print(f"HP:{hp:.0f}\nSTR:{str:.0f}")

character1 = createChar()

#mainloop\
state = ""
while True:
    state = input("type go to make anotha: ")
    if state == "go":
    
        
        break
        







