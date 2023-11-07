#https://www.youtube.com/watch?v=lRJ6AJkb4W0&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=62
#still have to elimate duplicates
import random
array = [[0,0,0,],[0,"BINGO",0],[0,0,0]]
used_numbers = ()

for i in range(0,3):
    for z in range(0,3):
        if array[i][z] != "BINGO":
            array[i][z] = random.randint(1, 99)
            

print(used_numbers)

a=(f"{array[0][0]:^4}|{array[0][1]:^8}|{array[0][2]:>4}")
b=(f"{array[1][0]:^4}|{array[1][1]:^7} |{array[1][2]:>4}")
c=(f"{array[2][0]:^4}|{array[2][1]:^8}|{array[2][2]:>4}")

total_lenght = len(a) +1

print(a)
print("-" * total_lenght)
print(b)
print("-" * total_lenght)
print(c)
