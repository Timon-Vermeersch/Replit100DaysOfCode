#https://www.youtube.com/watch?v=0YZqY_zQop4&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=157
from flask import Flask , request

app = Flask(__name__)


@app.route('/')
def index():
    
    return request.headers

app.run(host = '0.0.0.0', port = 81 )