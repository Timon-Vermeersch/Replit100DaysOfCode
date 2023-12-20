#https://www.youtube.com/watch?v=gTe4kHcFZJk&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=158

from flask import Flask, request, redirect
import os,dotenv,datetime
import sqlite3 as sq



TABLE_NAME_USER = "Users"
SELECT_SQL_USER = f"SELECT * FROM {TABLE_NAME_USER}"
INSERT_SQL_USER = f"""INSERT INTO {TABLE_NAME_USER}(user, password)
                 VALUES(?, ?)"""


TABLE_NAME = "Messages"
SELECT_SQL = f"SELECT * FROM {TABLE_NAME}"
INSERT_SQL = f"""INSERT INTO {TABLE_NAME}(number, message, author, time)
                 VALUES(?, ?, ?, ?)"""

local_db_path = r"86_blog\blog.db"
dotenv_path = ".devcontainer/devcontainer.env"
dotenv.load_dotenv(dotenv_path)

def connect_to_database():
    connection = sq.connect(local_db_path)
    cursor = connection.cursor()
    return connection, cursor

app = Flask(__name__)
app.sercret_key = os.environ['sessionKey']

@app.route("/")
def index():
    connection, cursor = connect_to_database()
    f = open("chat.html" , 'r' , encoding= 'utf-8')
    page = f.read()
    f.close()

    return page

app.run(host = '0.0.0.0' , port = 81,debug=True)

