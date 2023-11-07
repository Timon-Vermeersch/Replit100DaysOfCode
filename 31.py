#https://www.youtube.com/watch?v=rV6en_DUBZk&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=38
RED = "\033[031m"
BLUE = "\033[034m"
WHITE = "\033[1;37m"
END="\033[0m"
YELLOW = "\033[1;33m"
GREEN = "\033[0;32m"
LIGHT_PURPLE = "\033[1;35m"


def musicplayer():
    current_song = "queen"
    current_artist = "Radio gaga"

    text = "MUSIC APP"
    title = (f'{RED}{"="}{WHITE}{"="}{BLUE}{"="}{END}{text}{RED}{"="}{WHITE:^}{"="}{BLUE}{"="}{END}')
    print(f"         {title:^60}")
    print(f"🔥▶ {current_artist}")
    print(f"    {current_song}")
    next = "NEXT"
    prev = "PREV"
    pauze = "PAUZE"
    print(f"{prev:<60}")
    print(f"{GREEN}{next:^60}")
    print(f"{LIGHT_PURPLE}{pauze:>60}{END}")

def armbook():
    title = "WELCOME TO"
    header = "--  ARMBOOK  --"
    body1 = "definitly not a rip off of"
    body2 = "a certain other social"
    body3 = "networking site"
    title2 = "Honest"
    uname = "username:"
    pw= "password:"
    
    print(f"{title:^60}")
    print(f"{BLUE}{header:^60}")
    print(f"{body1:>60}")
    print(f"{body2:>60}")
    print(f"{body3:>60}")
    print(f"{RED}{title2:^60}")
    print(f"{END}{uname:^60}")
    print(f"{pw:^60}")


musicplayer()
armbook()