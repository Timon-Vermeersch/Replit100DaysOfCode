secpermin=int(60)
print("There are:",secpermin, "seconds in a minute")
secperhour= round(secpermin * 60,0)
print("there are:",secperhour, "seconds in an hour")
secperday= int(secperhour * 24)
print("there are:", secperday,"second in a day")
secperweek= int(secperday * 7)
print("there are:",secperweek, "in a week")
secperyear= int(secperweek * 52)
print("there are:",secperyear,"in a year")
addschrikkel=input("If you want it to be a schrikkeljaar, type ja: ")
if addschrikkel=="ja":
  answer= secperyear + secperday
  print ("in een schrikkeljaar zijn er: ",answer,"seconden" )
else: print("secperyear")











                 