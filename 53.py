#https://www.youtube.com/watch?v=n7Ot7Yi6xDw&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=82\
import os,time,traceback

# menu = add, view , remove
inventory = []
def removeItem():
    item = input("What item do you want to remove?: ").strip().lower().capitalize()
    if item in inventory:
        inventory.remove(item)
        print("removed!")
        time.sleep(1)
        os.system("cls")
    updateFile()
def updateFile():
	f = open("Inventory.txt","w")
	f.write(str(inventory))
	f.close()
              
def initFile():
    try:
        with open("Inventory.txt", "r") as f:
            file_contents = f.read()
            if file_contents:
                global inventory
                inventory = eval(file_contents)
            else:
                print("Inventory file is empty.")
    except FileNotFoundError:
        print("Inventory file not found.")
def addItem():
    print()
    item = input("Which item to add?: ").strip().lower().capitalize()
    inventory.append(item)
    print(item)
    print("Added!")
    time.sleep(1)
    updateFile()
    os.system("cls")    
def viewInventory():
    print()
    printed_items = set()
    for item in inventory:
        if item not in printed_items:
            count = inventory.count(item)
            print(f"{item}:{count}")
            printed_items.add(item)
    print("\n")
#--------------------------------------------
initFile()
while True: 
    menu  = input("""1. Add
2. View
3. Remove
> """)
    if menu =="1" or menu == "add":
        addItem()
    elif menu == "2" or menu == "view":
        viewInventory()
    elif menu == "3" or menu == "remove":
        removeItem()


