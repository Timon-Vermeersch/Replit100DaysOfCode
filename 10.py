bill=float(input("What was the bill?: "))
npeople= int(input("What's the amount of people that were there? "))
answer= bill/npeople
answer=round(answer,2)
print("We all owe 1 person ""€",answer, "excluding tip")


tip=float(input("What percentage do you want to tip?: "))


  
owed=round(answer/100*tip)
print (owed)
