#https://www.youtube.com/watch?v=M_Oy6fsirsA&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=173\

import os, dotenv, requests
from requests.auth import HTTPBasicAuth
from openai import OpenAI
from bs4 import BeautifulSoup

#setup
dotenv_path = ".devcontainer/devcontainer.env"
dotenv.load_dotenv(dotenv_path)
AIKEY = os.environ['OPENAI_API_KEY']

# scrape
#url = 'https://en.wikipedia.org/wiki/Urusei_Yatsura_(1981_TV_series)'
url = 'https://en.wikipedia.org/wiki/Piracy'
response = requests.get(url)
page = response.text
soup = BeautifulSoup(page, 'html.parser')

wiki = soup.find_all( 'div', {"class" : "mw-content-ltr mw-parser-output"})
wiki_ref = soup.find_all( 'div', { "class" : "mw-references-wrap mw-references-columns"})

#look for P
count = 1
result = ''
character_limit = 16000


for div in wiki:
    paragraphs = div.find_all('p')
    for paragraph in paragraphs:
        paragraph_text = paragraph.text
        if len(result) + len(paragraph_text) > character_limit:
            break
        result += paragraph_text

#look for reference
references = '' 
for div in wiki_ref:
    list_items = div.find_all('li')
    for li in list_items:
        anchors = li.find_all('a')
        for a in anchors:
            href = a.get('href') 
            if '#' not in href and '/wiki' not in href: 
                references += href
                references += '\n'






# ------------------------------------------------


question = "summarize in max three paragraphs "
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "you are a good wikipedia article condenser(tldr'r).'"},
        {"role": "user", "content": f" {question}: {result}"}
        ]
    )
reply = (completion.choices[0].message.content)




print(reply)
print()
print()
print(f'The references: \n{references}' , end = '\n ')