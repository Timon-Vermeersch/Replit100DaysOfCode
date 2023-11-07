#https://www.youtube.com/watch?v=O26Y99VRsgQ&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=42
toDo = ["sleep"]
item = ""

def printList():
	for i, item in enumerate(toDo,1):
		print(f"{i}. {item}")

def addToList():
	
	item = input("What to add to the list?: ")
	if item in toDo:
		print("Item already in list")
	else:
	    toDo.append(item)

def RemoveFromList():
    item = input("What to remove from the list?: ")
    removeBool = input("are you sure you want to remove? Type yes or no: ")
	
    if removeBool == "yes":
        if item in toDo:
           toDo.remove(item)
        else: 
             print("Cant remove. not in list")
    else: 
        print("nope")
        	
def editList():
	entry = int(input("which entry do you want to edit?: "))
	toDo[entry-1]= input(": ") 

def wipeList():
	toDo=[]
	print("wiped")
	
while True:
	menu = input("watchu wanna do? view, add, remove, edit or wipe?: ")
	if menu == "view" or menu =="1":
		printList()
	elif menu == "add"or menu == "2":
		addToList()
	elif menu == "remove"or menu =='3':
		RemoveFromList()
	elif menu == "edit"or menu =='4':
		editList()
	elif menu == "wipe"or menu =='5':
		wipeList()
	else:
		print("leer typen")
		break
		
