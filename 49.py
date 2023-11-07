#https://www.youtube.com/watch?v=kDQLt3V9WQE&t=61s
RED = "\033[031m"
BLUE = "\033[034m"
END="\033[0m"
filename = "hiscore.txt"
users = []
hiscores = []

def readFileFillArray():
    f = open(filename, "r")
    for line in f:
        data = line.strip().split(' ')
        users.append(data[0])
        hiscores.append(data[1])
    f.close()
readFileFillArray()

newScores = []
for n in hiscores:
    newScores.append(int(n))
hiscores = newScores


newSet = {}

for i in range(len(users)):
    newSet[users[i]] = newScores[i]

max_value = None
max_key = int()

for key,value in newSet.items():
    if max_value is None or value > max_value:
        max_value = value
        max_key = key

print(f"Current HiscoreHolder is: {RED}{max_key}{END} with a score of {BLUE}{max_value}{END}!")
