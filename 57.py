import time
num = int(input("type int: "))

def countBackWards(num):
    if num <= 0:
        print("done bish")
    else:
        for i in range(num):
            print("💯", end = "")
        print()
        countBackWards(num-1)

countBackWards(num)