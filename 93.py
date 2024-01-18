#https://www.youtube.com/watch?v=f1cx4qsor1I&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=172

import requests , json , os , dotenv
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv(r'.devcontainer\devcontainer.env')
clientID = os.environ['CLIENT_ID']
secretID = os.environ['CLIENT_SECRET']

url = 'https://accounts.spotify.com/api/token'
data = {'grant_type' : 'client_credentials'}
auth = HTTPBasicAuth(clientID, secretID)

response = requests.post(url , data = data, auth = auth)

# print(response.ok)
# print(response.json())
# print(response.status_code)

accessToken = response.json()['access_token']

artist = input("Enter Artist: ")
artist = artist.replace(" ", "%20" )
url_search = 'https://api.spotify.com/v1/search'
header = {"Authorization" : f"Bearer {accessToken}"}
search = f'?q=artist%3A{artist}&type=track&market=BE&limit=5'

fullurl = f"{url_search}{search}"
print(fullurl)

response2 = requests.get(fullurl , headers=header)
jsonSpo = response2.json()

for track in jsonSpo['tracks']['items']:
    print(track['name'])
    print(track['preview_url'])

