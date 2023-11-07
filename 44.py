#https://www.youtube.com/watch?v=483vwaq7qjo
listOfShame = []
def prettyPrint(): 
    print()
    for row in listOfShame:
        for item in row:
            print(f"{item:^10}", end= "  |  ")
        print()
    print()


while True : 
    menu = input("Add or Remove?: ")
    if menu.strip().lower()[0] == "a":

        name= input("whats your Name?: ")
        age = input("whats your Age?: ")
        pref = input("whats your Computa platform?: ")
        fname = name.lower().capitalize()
        row = [fname, age, pref]
        listOfShame.append(row)
    else:
        name = input("whats the name of the record?")
        for row in listOfShame:
            if name in row:
                listOfShame.remove(row)        
    prettyPrint()
prettyPrint()
    