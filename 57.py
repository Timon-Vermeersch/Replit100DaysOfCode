import time


def countBackwards(num):
    if num <= 0:
        print("done bish")
    else:
        for i in range(num):
            print("💯", end = "")
        print()
        countBackwards(num-1)

if __name__ == "__main__": 
    num = int(input("type int: "))
    countBackwards(num)