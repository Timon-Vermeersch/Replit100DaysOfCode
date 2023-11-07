#https://www.youtube.com/watch?v=VVMqAAMjO_I&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=32
import random
import os
import time as t

print("----------EPIC 1V1 BATTLE----------")


def rollHealth():
    d6 = random.randint(1,6)
    d8 = random.randint(1,8)
    hp = int((d6*d8)/2 + 12)
    return hp

def rollStrenght():
    d6 = random.randint(1,6)
    d12 = random.randint(1,12)
    strenght = int((d6*d12)/2 + 10 )
    return strenght

def createChar1():

    uname = input("enter char1 name: ")
    hp = rollHealth()
    strenght = rollStrenght()
    print(f"HP:{hp:.0f}\nSTR:{strenght:.0f}")
    print("-----------------------------------")
    return hp,strenght,uname

def createChar2():

    uname2 = input("enter char2 name: ")
    hp2 = rollHealth()
    str2 = rollStrenght()
    print(f"HP:{hp2:.0f}\nSTR:{str2:.0f}")
    t.sleep(1)
    return hp2,str2,uname2
    print("-----------------------------------")

#attribute export + fn init

character1 = createChar1()
character2 = createChar2()

hp,strenght, uname = character1
hp2,str2,uname2 = character2

print("--------------the battle---------------")
strdiff = (strenght - str2) +1
os.system("cls")
old_hp = int()
old_hp2 = int()
count = int(1)
while hp > 0 and hp2 > 0:

    #old_hp = hp
    #old_hp2 = hp2

    print(f"--------------Round {count} ---------------")
    t.sleep(1)
    print(f"{uname} HP:{hp}\n{uname2} HP:{hp2}\n  ")
    if strdiff > 0:
        hp2 -= strdiff
        count+=1
        t.sleep(0.5)
        #if hp == old_hp:
            #hp - 1
            #print(f"{uname} hit {uname2} for 1 damage\n")
        print(f"{uname} hit {uname2} for {strdiff} damage\n")
        t.sleep(1)
        
    elif strdiff < 0:
        hp -= abs(strdiff)
        count+=1
        t.sleep(0.5)
        #if hp2 == old_hp2:
            #hp2 - 1
            #print(f"{uname2} hit {uname} for 1 damage\n")
        print(f"{uname2} hit {uname} for {abs(strdiff)} damage\n")
        t.sleep(1)
        
    elif strdiff == 0:
        hp -= 1
        hp2 -= 1
        count+=1
        print(f"equal str of {strenght} and {str2}")
        t.sleep(1)
count -=1
print(f"--------------hoorah---------------")
if hp <= 0:
    print(f"{uname} was knocked out")
    print(f"{uname2} won in {count} turns")
elif hp2 <=0:
    print(f"{uname2} was knocked out")
    print(f"{uname} won in {count} turns")
print(f"--------------finish---------------\n")


    
    





        