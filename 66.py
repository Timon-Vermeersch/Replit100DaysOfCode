#https://www.youtube.com/watch?v=ddpOPyKymCQ&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=109


import tkinter as tk
#init window
window = tk.Tk()
window.title("Yo mama so fat")
window.geometry("190x230")

#def lambda: assignAsNumber(1)():
    

    


    # number = text.get("1.0","end")
    # number = int(number)
    # printVar += number
    # hello["text"] = printVar
        
#label
printVar = 0
displayNumber = tk.Label(text = printVar)
displayNumber.grid(row = 0, column= 1)

# #enter text
# text = tk.Text(window, height = 4, width = 25)
# text.grid(row = 0, column= 4)

currentTotal = 0
currentNumber = "" 


def assignInput(numberpressed):
    global currentTotal,currentNumber
    currentNumber += str(numberpressed)
    displayNumber["text"]  = currentNumber
    print(currentNumber)
def calculate():
    global currentNumber
    calculated = eval(currentNumber)
    print(calculated)
    displayNumber["text"]  = calculated
def clear ():
    global currentNumber
    currentNumber = "" 
    displayNumber["text"]  = currentNumber
def backspace ():
    global currentNumber

    currentNumber = currentNumber[:-1]
    displayNumber["text"]  = currentNumber
    print(currentNumber)

#nummersknoppen
button7 = tk.Button(text = "7",command=lambda : assignInput(7), width=4, height=2)
button7.grid(row = 1, column= 0, sticky="nsew")
button8 = tk.Button(text = "8",command=lambda : assignInput(8), width=4, height=2)
button8.grid(row = 1, column= 1, sticky="nsew")
button9 = tk.Button(text = "9",command=lambda: assignInput(9), width=4, height=2)
button9.grid(row = 1, column= 2, sticky="nsew")
button4 = tk.Button(text = "4",command=lambda: assignInput(4), width=4, height=2)
button4.grid(row = 2, column= 0, sticky="nsew")
button5 = tk.Button(text = "5",command=lambda: assignInput(5), width=4, height=2)
button5.grid(row = 2, column= 1, sticky="nsew")
button6 = tk.Button(text = "6",command=lambda: assignInput(6), width=4, height=2)
button6.grid(row = 2, column= 2, sticky="nsew")
button1 = tk.Button(text = "1",command=lambda: assignInput(1), width=4, height=2)
button1.grid(row = 3, column= 0, sticky="nsew")
button2 = tk.Button(text = "2",command=lambda: assignInput(2), width=4, height=2)
button2.grid(row = 3, column= 1, sticky="nsew")
button3 = tk.Button(text = "3",command=lambda: assignInput(3), width=4, height=2)
button3.grid(row = 3, column= 2, sticky="nsew")
button0 = tk.Button(text = "0",command=lambda: assignInput(0), width=4, height=2)
button0.grid(row = 4, column= 1, sticky="nsew")
#operatorknoppen
button_plus = tk.Button(text = "+",command=lambda: assignInput("+"), width=4, height=2)
button_plus.grid(row = 1, column= 3, sticky="nsew")
button_minus = tk.Button(text = "-",command=lambda: assignInput("-"), width=4, height=2)
button_minus.grid(row = 1, column= 4, sticky="nsew")
button_times = tk.Button(text = "x",command=lambda: assignInput("*"), width=4, height=2)
button_times.grid(row = 2, column= 3, sticky="nsew")
button_divide = tk.Button(text = "/",command=lambda: assignInput("/"), width=4, height=2)
button_divide.grid(row = 2, column= 4, sticky="nsew")
#knopforcalculate
button_equals = tk.Button(text = "=",command= calculate, width=4, height=2)
button_equals.grid(row = 5, column= 4, sticky="nsew")
#knopforclear
button_clear = tk.Button(text = "c", command = clear , width  = 4, height = 2)
button_clear.grid(row = 4, column = 4, sticky="nsew")
#knoforbackspace 
button_backspace = tk.Button(text = "<-", command = backspace , width  = 4, height = 2)
button_backspace.grid(row = 3, column = 4, sticky="nsew")


#mainloop
tk.mainloop()