#https://www.youtube.com/watch?v=Pg4QMSTTNIw&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=44
import os,time

listOfEmail = ["asians","whiteguys","africains","goths"]

def prettyPrint():
    os.system("cls")
    print("ListOfEmail")
    print("")
    for index in range(len(listOfEmail)):
        print(f"{index}: {listOfEmail[index]}")
    time.sleep(1)

def spam(max):
    os.system("cls")
    for i in range(0,len(listOfEmail)):
        print(f"""Email {i+1}

Dear {listOfEmail[i]}

get spammed kut
        """)
        time.sleep(3)
        os.system("cls")



while True:
    print("Spammer Inc.")
    menu = input("1: Add email\n2: Remove email\n3: Show emails\n4: Get spamming\n")
    if menu == "1":
        email = input("Email > ")
        print(email)
        listOfEmail.append(email)
    elif menu == "2":
        email = input("Email to remove > ")
        listOfEmail.remove(email)
    elif menu == "3":
        prettyPrint()
    elif menu == "4":
        spam(len(listOfEmail))
        
        
        
            

    time.sleep(1)
    os.system("cls")