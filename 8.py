print("Wholesome Positivity Machine")

username=input("Who are you?: ")
if username=="timon" or username=="Timon":
  print("Hi Timon!!")

goal=input("What do you want to achieve? ")
feeling=input("On a scale of 1-10 how do you feel today?: ")
print()

if  feeling=="1" or feeling=="2" or feeling=="3" or feeling=="4" or feeling=="5":
 print("Hey", username,"seems like you're not doing that great. get help soon!" )
elif feeling=="6":
     print("couldve been worse huh!")
else: print("Seems like you're doing fine")