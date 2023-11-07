print("Fill in the blank lyrics")
print("")
counter= 0
print("Nope Try again") and print(counter)
blank=""
while True:
  print()
  print("Never going to ____ you up")
  blank = input("answer: ")
  counter+= 1
  if blank == "give":
    break
         
     
  else: print("Nope Try again") 
print("correct! You're total amount of attempts was: ",counter)  