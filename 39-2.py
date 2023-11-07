#https://www.youtube.com/watch?v=g2Go3XS3VZg&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=54
import random, os, time

listOfWords = ["grapes","banana","apple","pear"]
lettersPicked = []
word = random.choice(listOfWords)
errorCount =0
tries = 0

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
    
allLetters = False
while errorCount < 6:
    letter = input("\nChoose a letter: \n").lower()


    if letter in lettersPicked:
        print("you've tried that before")
        continue
    lettersPicked.append(letter)


    if letter in word:
     print("\nYou found a letter\n")
    else:
        print("Nope, not in there")
        errorCount+=1



    allLetters = True
    for i in word:
        if i in lettersPicked:
            print(i, end="")
        else:
            print("_", end ="")
            allLetters = False
    
    if allLetters:
        print("\nYou won")
        break
        tries -=1
    printArt(errorCount)    
    tries +=1
    print(f"You tried this ({tries}) many time(s) with {errorCount} errors")

if errorCount == 6:
    print(f"You failed, this was the word: {word}")