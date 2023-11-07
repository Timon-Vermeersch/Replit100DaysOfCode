#https://www.youtube.com/watch?v=O26Y99VRsgQ&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=42
toDo = []
item = ""

def printList():
	for i, item in enumerate(toDo,1):
		print(f"{i}. {item}")

def addToList():
	item = input("What to add to the list?: ")
	toDo.append(item)

def RemoveFromList():
	item = input("What to remove from the list?: ")
	if item in toDo:
		toDo.remove(item)
	else: 
		print("Cant remove. not in list")


while True:
	menu = input("watchu wanna do? view, add or remove?: ")
	if menu == "view":
		printList()
	elif menu == "add":
		addToList()
	elif menu == "remove":
		RemoveFromList()
	else:
		print("leer typen")
		break
		
