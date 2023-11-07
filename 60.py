#https://www.youtube.com/watch?v=c6EmFRVulOY&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=97
#Themagicoftime
import datetime
import time

myDate = datetime.date(year = 2022, month = 12 , day = 12)


today = datetime.date.today()

deltaTime = datetime.timedelta(days = 365)

newDate = today + deltaTime
print(newDate)


vakantie = datetime.date(year = 2023,month = 12 , day = 25)

if vakantie > today:
    print("Coming soon")
elif vakantie < today:
    print("dyou have fun?")
else:
    print("hooray")
    


