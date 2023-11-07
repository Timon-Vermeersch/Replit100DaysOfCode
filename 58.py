#https://www.youtube.com/watch?v=ETz4WHtwKYE&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=93
#debugging

# 👉 Day 58 Challenge

#This challenge is all about using the debugger.

#Copy the broken code below into 'main.py' and use the debugger to help spot the mistakes in it. 


import random, os, time

totalAttempts = 0

def game():
  attempts = 0
  number = random.randint(1,100)
  while True:
    guess = int(input("Pick a number between 1 and 100: "))
    if guess > number:
      print("Too high")
      attempts+=1
    elif guess < number:
      print("Too low")
      attempts+=1
    else:
      print("Just right!")
      print(f"{attempts} attempts this round")
      return attempts

while True:
  menu = input("1: Guess the random number game\n2: Total Score\n3: Exit\n> ")
  if menu == "1":
    totalAttempts+= game()
  elif menu == "2":
    print(f"You've had {totalAttempts} attempts")
  else:
    break
