#https://www.youtube.com/watch?v=ITGtT9EEgL8&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=78
myEvents = []

f = open("calender.txt", "r")
myEvents = eval(f.read())
f.close()

def prettyPrint():
    print()
    for row in myEvents:
        print(f"{row[0]:^15} {row[1]:^15}")
    print()

while True:
    menu = input("1: Add, 2: Remove\n")
    if menu =="1":
        event = input("What event?: ").capitalize()
        date = input("What data?: ")
        row = [event, date]
        myEvents.append(row)
        prettyPrint()
    else:
        criteria = input("what event do you want to remove?: ").title()
        for row in myEvents:
            if criteria in row:
                myEvents.remove(row)
        prettyPrint()
    f = open("calender.txt","w")
    f.write(str(myEvents))
    f.close()

        