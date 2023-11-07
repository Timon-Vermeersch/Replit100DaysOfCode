#https://www.youtube.com/watch?v=KQ0hAk_lXCQ
import random as rd


snumber= rd.randint(1,10)
print(snumber,"\n")


foundNumber=False
guesses= 0

while foundNumber==False:
  
  guess= input("What is your guess?: ")
  
  
  
  if int(snumber)==int(guess):
    foundNumber==True 
    
    print()
    print("Correct!")
    print()

    #if 1 time else times
    if guesses==1:
      print("Took you",guesses,"wrongs")
    else: print("Took you",guesses,"wrongs")

  if foundNumber == False:
    guesses+=1


  elif int(guess) > int(snumber):
   print('Too high',"\n")
   
  
  elif int(guess) <0:
    print(guess,"kan niet kleiner dan 0 zijn")
    
    exit()
  elif int(guess) < int(snumber):
    print('Too low',"\n")
    

  elif guess != int():
    print("guess niet gelijk aan int")
  print()

    
#if snumber

