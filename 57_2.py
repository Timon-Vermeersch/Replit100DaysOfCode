#factorial
#https://www.youtube.com/watch?v=37DuuZxWX1o&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=91


def factorial():
    factorial = int(input("enter factorial: "))
    result = 1

    if factorial <= 0:
        print("done")
    else:
        
        for i in range(1,factorial +1):
            result *= i 
        
factorial()