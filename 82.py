#https://www.youtube.com/watch?v=h1PgRJA6Wco&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=149
from flask import Flask, request

app = Flask(__name__)


@app.route("/" , methods = ['GET'])
def index():
    page_eng = 'oi m8 welc0me'
    page_nl = 'Yo kut'
    get =  request.args
    if get["lang"].lower() == 'eng':
        return page_eng
    if get["lang"].lower() == "nl":
        return page_nl
    return "No data"

app.run(host = '0.0.0.0' , port=81)