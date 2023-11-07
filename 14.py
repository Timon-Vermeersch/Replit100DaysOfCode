print("LOCAL VERSUS ROCK PAPER SCISSOR")
print("")
templatechoice=str("""
1. Rock
2. Paper
3. Scissor
  """)

username1=input("What's your name player 1?: ")
print("")
username2=input("And player 2's name?:")
print("")
print(username1,"you are player 1,",username2,"you are player 2")
print("")


print(username1,'?')
answer1=input(templatechoice)
print("")
print(username2,'?')
answer2=input(templatechoice)
print("")


#gelijkspel
if (answer1==("1") or answer1==("Rock")) and (answer2==("1") or answer2==("Rock")):
  print("Both took rock, you both suck.") 
elif (answer1==("2") or answer1==("Paper")) and (answer2==("2") or answer2==("Paper")):
  print("Both took Paper, you both suck.") 
elif (answer1==("3") or answer1==("Scissor")) and (answer2==("3") or answer2==("Scissor")):
  print("Both took Scissor, you both suck.")
  
#u1 won
elif (answer1==("1") or answer1==("Rock")) and (answer2==("3") or answer2==("Scissor")):
  print(username1,"won by picking rock")
elif (answer1==("3") or answer1==("Scissor")) and (answer2==("2") or answer2==("Paper")):
  print(username1,"won by picking scissor")
elif (answer1==("2") or answer1==("Paper")) and (answer2==("1") or answer2==("Rock")):
  print(username1,"won by picking Paper")
  
#u2 won
elif (answer1==("3") or answer1==("Scissor")) and (answer2==("1") or answer2==("Rock")):
  print(username2,"won by picking rock")
elif (answer1==("1") or answer1==("Rock")) and (answer2==("2") or answer2==("Paper")):
  print(username2,"won by picking paper")
elif (answer1==("2") or answer1==("Paper")) and (answer2==("3") or answer2==("Scissor")):
  print(username2,"won by picking scissor")



  


#if answer1==answer2: print("both took",answer1)  
else: print("fu")
print("")
print(answer1,"and",answer2,'were picked in this game')

  
  










