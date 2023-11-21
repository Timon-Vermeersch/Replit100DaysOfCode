import tkinter as tk
from PIL import Image, ImageTk
import os
if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))
    print(f" \u001b[31m {script_directory}\u001b[37m")
    window = tk.Tk()
    window.title("Timon's waifu selector")
    window.geometry("600x1000")


    def selectimage():
        print("")
        canvas.itemconfig(selectedPhoto, image=misato)

#inputkader
    choice = tk.Text(window , height =  1 , width = 20)
    choice.pack()
#createButton
    button = tk.Button(text="Seek!!", command =  selectimage)
    button.pack()
#createcanvas
    canvas = tk.Canvas(window, height=900 , width = 600)
    canvas.pack()
#createimages
    asuna = Image.open(r"C:\Users\timon\Documents\shitcoding\Replit\Working67\Asuna.jpeg")
    asuna = ImageTk.PhotoImage(asuna)

    misato = Image.open(os.path.join(os.path.dirname(__file__), r"Misato.jpeg"))
    misato = ImageTk.PhotoImage(misato)

    sakuya = Image.open(os.path.join(os.path.dirname(__file__), r"Sakuya.jpeg"))
    sakuya = ImageTk.PhotoImage(sakuya)

    seras = Image.open(os.path.join(os.path.dirname(__file__), r"Seras.jpeg"))
    seras = ImageTk.PhotoImage(seras)

    yoru = Image.open(os.path.join(os.path.dirname(__file__), r"Yoru.png"))
    yoru = ImageTk.PhotoImage(yoru)

    zero = Image.open(os.path.join(os.path.dirname(__file__), r"Zero.jpeg"))
    zero = ImageTk.PhotoImage(zero)

    selectedPhoto = canvas.create_image(0,0,anchor = "nw",image = asuna)


    
    tk.mainloop()