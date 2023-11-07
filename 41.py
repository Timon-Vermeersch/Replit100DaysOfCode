#https://www.youtube.com/watch?v=MENfSTbAcn8&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=56

site = {"Name":"None","url":"None","desc":"None","rating":"None"}

def printDict():
    for name,value in site.items():
        print(f"{name}: {value}")

for name, value in site.items():
    new = input(f"What's the {name} of the site?: ")
    site[name] = new
printDict()
