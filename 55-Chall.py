#https://www.youtube.com/watch?v=ITGtT9EEgL8&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=78
toDo = ["sleep"]
item = ""
import os
f = open("Todo.txt","r")
toDo = eval(f.read())
f.close()

def makeBackup():
	#check folder
	if not os.path.exists("backups"):
		os.mkdir("backups")
		print("folder backups created")
	else:
		print("backup folder present!")
	#set path4file
	filename = os.path.join("backups/","backup.txt")
    #createFileandwrite
	x = open(filename, "w")
	x.write(str(toDo))
	x.close()
	
def updateFile():
	f = open("Todo.txt","w")
	f.write(str(toDo))
	f.close()
	
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
		makeBackup()
	elif menu == "add"or menu == "2":
		addToList()
		makeBackup()
		updateFile()
	elif menu == "remove"or menu =='3':
		RemoveFromList()
		makeBackup()
		updateFile()
	elif menu == "edit"or menu =='4':
		editList()
		makeBackup()
		updateFile()
	elif menu == "wipe"or menu =='5':
		wipeList()
		makeBackup()
		updateFile()
	else:
		print("leer typen")
		break
		



