#https://www.youtube.com/watch?v=sylq300J9EM&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=40
import random
greetings=["olá","namaste","merhaba","hallo","xin chào","salaam","dzień dobry","bonjour"]

for count in range(0,100):

    int = random.randint(0,7)
    print(f"\033[0;3{int}m{greetings[int]}")
    
