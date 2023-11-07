#https://www.youtube.com/watch?v=b2NlupcxRew
#HiscoresStorage
three_letter_initial = ""

f = open("hiscore.txt", "a+")
while three_letter_initial != "q":

    three_letter_initial = input("three_letter_initial?/To quit type q: ")

    if three_letter_initial == "q":
        break
    else:
        hiScore = input("whats your high score?: ")
    

    f.write(f"{three_letter_initial}\t{hiScore}\n")
    f.close()

