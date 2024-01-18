#https://www.youtube.com/watch?v=f1cx4qsor1I&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=172

from flask import Flask, request, redirect , session , json 
import os, dotenv
import requests
from requests.auth import HTTPBasicAuth

dotenv_path = ".devcontainer/devcontainer.env"
dotenv.load_dotenv(dotenv_path)

clientID = os.environ['CLIENT_ID']
secretID = os.environ['CLIENT_SECRET']

app = Flask(__name__)
app.secret_key = os.environ['sessionKey']






@app.route("/")
def index():
    f = open("93_SpotifyApi/index.html" , 'r')
    page = f.read()
    f.close()
    return page
@app.route("/search", methods = ['POST'])
def search():
    f = open("93_SpotifyApi/index.html" , 'r')
    page = f.read()
    f.close()
    form = request.form
    year = form['jaar']
    url = 'https://accounts.spotify.com/api/token'
    data = {'grant_type' : 'client_credentials'}
    auth = HTTPBasicAuth(clientID, secretID)
    response = requests.post(url , data = data, auth = auth)
    accessToken = response.json()['access_token']
    url_search = 'https://api.spotify.com/v1/search'
    header = {"Authorization" : f"Bearer {accessToken}"}
    search = f'?q=year%3A{year}&type=track'
    fullurl = f"{url_search}{search}"
    response2 = requests.get(fullurl , headers=header)
    jsonSpo = response2.json()
    tracks_html = ''
    for track in jsonSpo['tracks']['items']:
        song = track['name']
        prurl = track['preview_url']
        
        tracks_html += f""" <section>
            <div>{song}['name']</div>
            <audio controls>
        <source src="{prurl}" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
        </section>
        <hr>
        """
    
    # print(jsonSpo)
    page = page.replace("{supbro}" , tracks_html)

    return page
    


    




app.run(host = '0.0.0.0' , port = 81,debug=True)

