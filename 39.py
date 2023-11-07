#https://www.youtube.com/watch?v=g2Go3XS3VZg&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=53
import random
import os
import time
tries = 1
errorCount = 0
wordsList = ["aapje", "mongool","zuster"]
word_to_guess = random.choice(wordsList)
lettersPicked = []

def revealedWords():
    for i in range(0,len(word_to_guess)):
        print("_", end = "")


    

def printArt(errorCount):
    print("")
    art = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    print(art[errorCount])

def printLettersFound(word_to_guess): 
    print("lorem")


allLetters = False
while tries < 8:
    os.system("cls")
    
    guess = input("Choose a letter: ").lower()

    if guess in lettersPicked:
        print("You've already tried that")
        continue  

    lettersPicked.append(guess)


    if guess in word_to_guess:
        print("correct, you found a letter")
    else:
        print("Nope, not in there")
        tries+=1
        errorCount+=1

    if allLetters:
        print("You found it!")
        break

    if tries >= 7:
        print(f"You lost, the word was {word_to_guess}")
    else: 
        if tries == 1:
            print(f"You've tried once, max 7")
        else: 
            print(f"You've tried {tries-1} times, max 7")
    time.sleep(3)    
    printArt(errorCount)    
    
    

   

           

