#https://www.youtube.com/watch?v=jPF_tAnYY44
print("----character health thingy----")


counter = int(0)
count = int(input("# of chars?: "))


def rollHp():
    import random
    uname = input("enter char name: ")
    d6 = random.randint(1,6)
    d8 = random.randint(1,8)
    hp = d6*d8
   
    return hp, d6, d8, uname

while counter < count:
    myHp,d6,d8,uname = rollHp()
    counter+=1
    print(f"{uname}'s hp is {myHp} decided by a {d6}, times a {d8} " )
