#https://youtu.be/c6EmFRVulOY?list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0
#datetimeeventstuff
import datetime


dag = input("Dag?: ")
maand = input("Maand?: ")
jaar = input("Jaar?: ")

dag,maand,jaar = int(dag) , int(maand) , int(jaar)



today = datetime.date.today()
event = datetime.date(jaar,maand,dag)

dagDelta = datetime.date.today() - event


if event > today:
    print(f"Coming soon, in about {abs(dagDelta.days)} days")
elif event < today:
    print(f"Missed it about {abs(dagDelta.days)} days")
else:
    print("hooray")
    




