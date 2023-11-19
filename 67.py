import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Eva bitch")
window.geometry("800x600")

def changeImage():
    canvas.itemconfig(container, image=newImage)

hello = tk.Label(text="Yo")
hello.pack()

button = tk.Button(text="Click me", command=changeImage)
button.pack()

canvas = tk.Canvas(window, height=500, width=500)
canvas.pack()

image = Image.open("eva.png")
image = ImageTk.PhotoImage(image)

newImage = Image.open("Yoru.png")
newImage = ImageTk.PhotoImage(newImage)

container = canvas.create_image(-60, 50, anchor="nw", image=image)

tk.mainloop()
