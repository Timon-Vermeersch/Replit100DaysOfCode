#https://www.youtube.com/watch?v=ddpOPyKymCQ&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=109


import tkinter as tk
#init window
window = tk.Tk()
window.title("Yo mama so fat")
window.geometry("190x230")

#def lambda: assignAsNumber(1)():
    

    


    #number = text.get("1.0","end")
    #number = int(number)
    #printVar += number
    #hello["text"] = printVar
    
#label
printVar = 0
displayNumber = tk.Label(text = printVar)
displayNumber.grid(row = 0, column= 1)

# #enter text
# text = tk.Text(window, height = 4, width = 25)
# text.grid(row = 0, column= 4)
currentNumberList = []
currentTotal = 0
currentNumber = "" 


def assignInput(numberpressed):
    global currentTotal,currentNumber
    if numberpressed in [1,2,3,4,5,6,7,8,9,0]:
        currentNumber += str(numberpressed)
        print(currentNumber)
    elif assignInput == "+":
        plus = []
        print(currentTotal)
        

#nummersknoppen
button7 = tk.Button(text = "7",command=lambda : assignInput(7), width=4, height=2).grid(row = 1, column= 0)
button8 = tk.Button(text = "8",command=lambda : assignInput(8), width=4, height=2).grid(row = 1, column= 1)
button9 = tk.Button(text = "9",command=lambda: assignInput(9), width=4, height=2).grid(row = 1, column= 2)
button4 = tk.Button(text = "4",command=lambda: assignInput(4), width=4, height=2).grid(row = 2, column= 0)
button5 = tk.Button(text = "5",command=lambda: assignInput(5), width=4, height=2).grid(row = 2, column= 1)
button6 = tk.Button(text = "6",command=lambda: assignInput(6), width=4, height=2).grid(row = 2, column= 2)
button1 = tk.Button(text = "1",command=lambda: assignInput(1), width=4, height=2).grid(row = 3, column= 0)
button2 = tk.Button(text = "2",command=lambda: assignInput(2), width=4, height=2).grid(row = 3, column= 1)
button3 = tk.Button(text = "3",command=lambda: assignInput(3), width=4, height=2).grid(row = 3, column= 2)
button0 = tk.Button(text = "0",command=lambda: assignInput(0), width=4, height=2).grid(row = 4, column= 1)
#operatorknoppen
button_plus = tk.Button(text = "+",command=lambda: assignInput("+"), width=4, height=2).grid(row = 1, column= 3)
button_minus = tk.Button(text = "-",command=lambda: assignInput("-"), width=4, height=2).grid(row = 1, column= 4)
button_times = tk.Button(text = "x",command=lambda: assignInput("*"), width=4, height=2).grid(row = 2, column= 3)
button_divide = tk.Button(text = "/",command=lambda: assignInput("/"), width=4, height=2).grid(row = 2, column= 4)
#knopforcalculate
button_equals = tk.Button(text = "=",command=lambda: assignInput("="), width=4, height=2).grid(row = 3, column= 4)

#mainloop
tk.mainloop()