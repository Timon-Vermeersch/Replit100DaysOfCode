#https://www.youtube.com/watch?v=ZlcldFE4BeY&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=80
#pizzaShop
order = []
try:
    f = open("order.txt", "r")
    order = eval(f.read())
    f.close()
except:
    print("filenotfound")

def updateFile():
	f = open("order.txt","w")
	f.write(str(order))
	f.close()

def addPizza():
    print("")
    name = input("whats your name?\n: ").strip().lower()
    pizza = input("Ham and Cheese OR Meat Feast?\n: ").strip().lower()
    size = input("S/M/L?\n: ").strip().lower()
    try:
        quantity = int(input("how many?\n: ").strip().lower())
    except ValueError:
        print("enter valid int")
        quantity = int(input("how many?\n: ").strip().lower())

    price = int()
    total = ""
    if size == "s":
        price = 10
    elif size == "m":
        price = 15
    elif size == "l":
        price  = 20
    
    total = price * int(quantity)
    total = round(total,2)

    row = [name, pizza, size, quantity, total]
    order.append(row)
    print(row)
    updateFile()
def viewPizza():
    print()
    print(f"{'Naam':^20} {'pizza':^20} {'size':^12} {'amount':^12} {'total in €':^12}")
    for row in order:
        print(f"{row[0]:^20} {row[1]:^20} {row[2]:^12} {row[3]:^12} {row[4]:^12}")
    print()


while True:
    menu  = input("1: Add Pizza\n2: View pizza\n> ")
    if menu == "1":
        addPizza()
    elif menu == "2":
        viewPizza()