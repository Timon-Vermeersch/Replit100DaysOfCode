#https://www.youtube.com/watch?v=9mnn6qAzrBw&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=168

import requests , json

#print(json.dumps(user,indent=2))
for i in range(0,9):
    result = requests.get('https://randomuser.me/api/')
    user = result.json()
    for person in user["results"]:
        name = f"""{person["name"]["first"]} {person["name"]["last"]}""" 
        image = f"""{user["results"][0]["picture"]["large"]}"""

        print(name)

        namejpg = name.replace(" ", "")
        picture = requests.get(image)

        f = open(f"{namejpg}.jpg" , 'wb')
        f.write(picture.content)
        f.close()
        