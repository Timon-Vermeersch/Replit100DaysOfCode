#https://www.youtube.com/watch?v=uaOmD6XRt3A
import os
import time
def enquette():
    answers={}
    for i in range(1,31):
        print(f"Day {i}:")
        answer = input(f"\033[32m")

        answers[i] = answer
        print(f"\033[0m{'You thought:':^21}\n{answers[i]:^21}")  
        time.sleep(2)
        os.system("cls")
enquette()