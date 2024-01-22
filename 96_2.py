#https://www.youtube.com/watch?v=XH4VcY7tRGI&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=183

import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/'
url2 = 'https://news.ycombinator.com/?p=2'
url3 = 'https://news.ycombinator.com/?p=3'
url4 = 'https://news.ycombinator.com/?p=4'

response = requests.get(url) 
page = response.text
response = requests.get(url4) 
page += response.text 
response = requests.get(url2) 
page +=response.text  
response = requests.get(url3) 
page += response.text  


soup = BeautifulSoup(page, 'html.parser')
hackernews = soup.find_all('span' , {"class" : 'titleline'})

print()
for items in hackernews:
    if 'Python' in items.text or 'python' in items.text:
        print(items.text)
        link = items.find('a')
        print(link['href'])
        print()

 



