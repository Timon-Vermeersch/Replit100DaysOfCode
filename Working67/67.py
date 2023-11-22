from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
import os
if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))
    print(f" \u001b[31m {os.path.dirname}\u001b[37m")
    window = tk.Tk()
    window.title("Timon's waifu selector")
    window.geometry("600x1000")

    
    def on_click():
        messagebox.showerror('Python Error', 'Person not in list')
                
    def selectimage():

        canvas.delete("all")
        choiceInputText = choiceInput.get("1.0","end-1c").strip().lower()
        check = choices.get(choiceInputText)
        
        if check != None: 
            canvas.create_image(0,0,anchor = "nw", image = check)
        else:
            on_click()
            
            
            
    
#inputkader
    choiceInput = tk.Text(window , height =  1 , width = 20)
    choiceInput.pack()
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


    choices = {"asuna": asuna,"misato" : misato , "sakuya": sakuya, "seras" : seras ,"yoru" : yoru, "zero" : zero}


    currentPhoto = zero

    print(f"{currentPhoto}")


    selectedPhoto = canvas.create_image(0,0,anchor = "nw",image = currentPhoto )

    
    tk.mainloop()