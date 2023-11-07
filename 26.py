#https://www.youtube.com/watch?v=_IGpC-sA7M4&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=29
import os 
import time as t
def clearScreen():
    for i in range (1,1000):
        print(i)
        t.sleep(0.3)
        os.system("cls")
CS = clearScreen()
print(CS)