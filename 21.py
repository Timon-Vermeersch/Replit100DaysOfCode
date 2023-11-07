#https://youtu.be/rfK_QXsf2PA
#MATHGAME

import tkinter as tk

window = tk.Tk()

while True: 
    multiples = float(input("name your multiples: "))
    print(f"Cool, tafel van {multiples:.0f} ")
    triedC = 0
    for i in range(1,11,1):
        while True:
            try:
                gebruiker_antwoord =  input(f"{i} x {multiples:.0f} = ")
                verwacht_antwoord = i * multiples

                if gebruiker_antwoord == "skip":
                    break
                    
                if int(gebruiker_antwoord) == verwacht_antwoord:
                    print("correct\n")
                    break
                else: 
                    print("wrong! Try again.\n") 
                    triedC += 1
            except ValueError: 
                if gebruiker_antwoord == "skip":
                    break
                    i == 11
                    
                    
                else:
                    print("valueError, enter valid integer")

    print(f"wrongs counter: {triedC}\n")
    print("goed gedaan je krijgt nu een kusje van japser\n")
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("K!")
        break

 
window.mainloop()


