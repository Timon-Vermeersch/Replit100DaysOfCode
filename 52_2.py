import traceback
debugMode = True
myStuff = []


try: 
    f = open("stuff.mine", "r")
    myStuff = eval(f.read())
    f.close()
except: 
    print("Error:UNREADABLE")
    if debugMode:
        print(traceback)

for row in myStuff:
    print(row)