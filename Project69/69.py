import tkinter as tk
from PIL import Image, ImageTk
import os
import time


if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))
    print(f" \u001b[31m {os.path.dirname}\u001b[37m")
    window = tk.Tk()
    window.title("TifaVisualNovel")
    window.geometry("700x700")

    canvas = tk.Canvas(window, height=520 , width = 525)
    
    
    #createImages
    tifabanana = Image.open(os.path.join(os.path.dirname(__file__), r"tifabanana.jpeg"))
    tifabanana = ImageTk.PhotoImage(tifabanana)

    tifabanana2 = Image.open(os.path.join(os.path.dirname(__file__), r"tifabanana2.jpeg"))
    tifabanana2 = ImageTk.PhotoImage(tifabanana2)

    tifagame = Image.open(os.path.join(os.path.dirname(__file__), r"tifagame.jpeg"))
    tifagame = ImageTk.PhotoImage(tifagame)

    tifahall = Image.open(os.path.join(os.path.dirname(__file__), r"tifahall.jpeg"))
    tifahall = ImageTk.PhotoImage(tifahall)


    tifalaptop = Image.open(os.path.join(os.path.dirname(__file__), r"tifalaptop.jpeg"))
    tifalaptop = ImageTk.PhotoImage(tifalaptop)

    tifatablet = Image.open(os.path.join(os.path.dirname(__file__), r"tifatablet.jpeg"))
    tifatablet = ImageTk.PhotoImage(tifatablet)

    tifausb = Image.open(os.path.join(os.path.dirname(__file__), r"tifausb.jpeg"))
    tifausb = ImageTk.PhotoImage(tifausb)

    
    def start():
        global selectedPhoto
        for widget in window.winfo_children():
            widget.destroy()
        canvas = tk.Canvas(window, height=520, width=525)
        canvas.pack()
        label = tk.Label(text = "You meet Tifa at COE meetup IRL")
        label.pack()
        selectedPhoto = canvas.create_image(10,0,anchor = "nw",image = tifahall )
        button = tk.Button(text=">Hello Tifa! whats ur highest pp play?", command =  start1)
        button.pack()
        button2 = tk.Button(text=">Hello Tifa! Do you play tablet or mouse???", command =  start2_1)
        button2.pack()

    def start1():
        global selectedPhoto, canvas, window
        for widget in window.winfo_children():
            widget.destroy()
        canvas = tk.Canvas(window, height=520, width=525)
        canvas.pack()
        label = tk.Label(window, text="Tifa whips out her laptop and says: '727 bro'")
        label.pack()
        selectedPhoto = canvas.create_image(10, 0, anchor="nw", image=tifalaptop)
        button = tk.Button(window, text=">Yo what?! that's a cool laptop!", command=start1_1)
        button.pack()
        button2 = tk.Button(window, text=">Damn Tifa! That is one BIG laptop!", command=banana)
        button2.pack()
    


    def start1_1():
        global selectedPhoto, canvas, window
        for widget in window.winfo_children():
            widget.destroy()
        canvas = tk.Canvas(window, height=520, width=525)
        canvas.pack()
        label = tk.Label(window, text="Tifa smiles and starts showing you her USB ports :3")
        label.pack()
        selectedPhoto = canvas.create_image(10, 0, anchor="nw", image=tifausb)
        label1 = tk.Label(window, text="The end")
        label1.pack()
        button = tk.Button(window, text=">Restart!", command=start)
        button.pack()


    def banana():
        global selectedPhoto, canvas, window
        for widget in window.winfo_children():
            widget.destroy()
        canvas = tk.Canvas(window, height=520, width=525)
        canvas.pack()
        label = tk.Label(window, text="Tifa smirks whips out her banana and PUNCHES you with it")
        label.pack()
        selectedPhoto = canvas.create_image(10, 0, anchor="nw", image=tifabanana)
        label1 = tk.Label(window, text="The end")
        label1.pack()
        button = tk.Button(window, text=">Restart!", command=start)
        button.pack()
    def banana2():

        global selectedPhoto, canvas, window
        for widget in window.winfo_children():
            widget.destroy()
        canvas = tk.Canvas(window, height=520, width=525)
        canvas.pack()
        label = tk.Label(window, text="'She whips out a banana and punches you in the face. ")
        label.pack()
        selectedPhoto = canvas.create_image(10, 0, anchor="nw", image=tifabanana2)
        label1 = tk.Label(window, text="The end")
        label1.pack()
        button = tk.Button(window, text=">Restart!", command=start)
        button.pack()
        
    def start2_1():
        global selectedPhoto, canvas, window
        for widget in window.winfo_children():
            widget.destroy()
        canvas = tk.Canvas(window, height=520, width=525)
        canvas.pack()
        label = tk.Label(window, text="Tifa whips out her osu tablet")
        label.pack()
        selectedPhoto = canvas.create_image(10, 0, anchor="nw", image=tifatablet)
        button = tk.Button(window, text=">What?! You play with tablet? That's so cool!!", command=start2_1_1)
        button.pack()
        button2 = tk.Button(window, text=">Mouse??? Wtf are you gay?", command=banana2)
        button2.pack()
    def start2_1_1():
        global selectedPhoto, canvas, window
        for widget in window.winfo_children():
            widget.destroy()
        canvas = tk.Canvas(window, height=520, width=525)
        canvas.pack()
        label = tk.Label(window, text="'I Doooooo!!!' she yells, and together you play osu forever and ever ❤️ ")
        label.pack()
        selectedPhoto = canvas.create_image(10, 0, anchor="nw", image=tifagame)
        label1 = tk.Label(window, text="The end")
        label1.pack()
        button = tk.Button(window, text=">Restart!", command=start)
        button.pack()


    canvas.pack()
    start()
    
    tk.mainloop()

