#https://www.youtube.com/watch?v=ONBbX6Qz2k4&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=95
#Checkifpalindrome



woord = input("> ").strip().lower()

def isPalindrome(woord, pos = 0, ypos = 1 , x = 0):
    
    if woord[pos] == woord[len(woord)-ypos]:
        print(f"TRUE{pos}")
        pos +=1
        ypos+=1
        x +=1
        if x == len(woord):
            print("yes palalal")
            quit()
        else:
            isPalindrome(woord, pos, ypos, x)
    else:
        print("not palalila")

isPalindrome(woord)