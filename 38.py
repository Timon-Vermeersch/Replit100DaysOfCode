#https://www.youtube.com/watch?v=twzCfSvyte8&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=52

sentence = "for every bear i know there's always a big fat retard running around"

def colorChange(): 
    if letter.lower() == "b":
        print('\033[34m', end = "")
    elif letter.lower() == "r":
        print('\033[31m', end = "")
    elif letter.lower() == "y":
        print('\033[35m', end = "")
    elif letter.lower() == "g":
        print('\033[32m', end = "")
    elif letter == " ":
        print('\033[0m', end = "")

for letter in sentence:
    colorChange()
    print(letter, end = '')
    
