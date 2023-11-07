print("Exam Grade Calculator")
print()

name=input("What's the name of the test?: ")

maxsco= float(input("What's the maximum possible score: "))
 
sco=float(input("What score number did you get?: "))
percent=float((sco/maxsco) * 100)
round(percent)

grade=str()
if percent <=100 and percent>=90: 
  grade=("A+")
elif percent <=89 and percent >=80:
  grade=("A")
elif percent <=79 and percent >=70:
  grade=("B")
elif percent <=69 and percent >=60:
  grade=("C")
elif percent <=59 and percent >=50:
  grade=("D")
elif percent <=50:
  grade=("incompetent")

else:
  print("you suck bro")

print("That means you got a",percent,"%. The grade you get is a:",grade,)