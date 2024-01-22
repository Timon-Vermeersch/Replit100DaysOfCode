#https://www.youtube.com/watch?v=zQl-0RihxUw&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=171


import os, dotenv, requests
from requests.auth import HTTPBasicAuth
from openai import OpenAI

dotenv_path = ".devcontainer/devcontainer.env"
dotenv.load_dotenv(dotenv_path)

clientID = os.environ['CLIENT_ID']
secretID = os.environ['CLIENT_SECRET']
KEY = os.environ['NEWS_KEY']
AIKEY = os.environ['OPENAI_API_KEY']



url = 'https://newsapi.org/v2/everything'

response = requests.get(f'https://newsapi.org/v2/top-headlines?country=nl&apiKey={KEY}')
newsjson = response.json()

for news in newsjson['articles']:
    articles = f""" 
{news['title']}
{news['description']}
 """
    

    message = articles
    question = "summarize every article MAXIMUM 3 words, finish with "

    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Your an ai an take in new article titles and condenses them into 3 words or less.'"},
        {"role": "user", "content": f" {question}: {articles}"}
        ]
    )
    reply = (completion.choices[0].message.content)
    reply = reply.replace("'", "" )
    print(reply)
    zoek = reply.replace(' ' , '+')
    print(zoek)
    
    

    url = 'https://accounts.spotify.com/api/token'
    data = {'grant_type' : 'client_credentials'}
    auth = HTTPBasicAuth(clientID, secretID)
    response = requests.post(url , data = data, auth = auth)
    accessToken = response.json()['access_token']

    url_search = 'https://api.spotify.com/v1/search'
    header = {"Authorization" : f"Bearer {accessToken}"}
    search = f'?q={zoek}&type=track&limit=1'
    fullurl = f"{url_search}{search}"
    response2 = requests.get(fullurl , headers=header)
    jsonSpo = response2.json()
    for track in jsonSpo['tracks']['items']:
        try:
            print(track['external_urls']['spotify'])
            print()
        except Exception as e:
            print("error")
        


