#https://www.youtube.com/watch?v=_SOBP3pJ4uk&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=113
#hide and show

import tkinter as tk

window = tk.Tk()
window.title("Hello")
window.geometry("400x400")

labelOn = True
def hideLabel():
    global labelOn
    global button

    if labelOn:
        label.pack_forget()
        button.pack_forget()
        labelOn = False
        button = tk.Button(text = "Reveal me?" ,command = hideLabel)
        
        button.pack()
    elif labelOn == False:
        button.pack_forget()
        label.pack()
        button = tk.Button(text = "clikc me" ,command = hideLabel)
        button.pack()
        labelOn = True


label =  tk.Label(text = "hide text?")
label.pack()

button = tk.Button(text = "clikc me" ,command = hideLabel)
button.pack()
tk.mainloop()