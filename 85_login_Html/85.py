#https://www.youtube.com/watch?v=g5JOQvR8xUE&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=151
##for future: sqlite3 MyFirstDatabase.db "CREATE TABLE diary (date TEXT PRIMARY KEY, entry TEXT NOT NULL);"
from flask import Flask, request, redirect,flash,render_template, session
import sqlite3 as sq
import dotenv
import os

TABLE_NAME = "Users"
SELECT_SQL = f"SELECT * FROM {TABLE_NAME}"
INSERT_SQL = f"""INSERT INTO {TABLE_NAME}(user, pw)
                 VALUES(?, ?)"""


local_db_path = "84_login_Html\dag84.db"
#env
dotenv_path = ".devcontainer/devcontainer.env"
dotenv.load_dotenv(dotenv_path)

def connect_to_database():
    connection = sq.connect(local_db_path)
    cursor = connection.cursor()
    return connection, cursor

app = Flask(__name__,template_folder='templates')
app.secret_key = os.environ['sessionKey']

@app.route("/" , methods = ['GET'])
def index():
    f = open("84_login_Html\greeting.html" , 'r' , encoding = "utf-8")
    page = f.read()
    f.close
    myName = ''
    if session.get("myName"):
        print('sessionfound')
        myName = session["myName"]
        print(f'aangemeld{myName}')
        #return redirect ('/welcome')
    return page

@app.route("/signup")
def signup():
    f = open("84_login_Html\signup.html" , 'r' , encoding= "utf-8")
    page = f.read()
    f.close
    return page



@app.route("/processSignup" , methods = ['POST'])
def processSignup():
    connection,cursor = connect_to_database()
    wachtwoord = ''
    username = ''
    form = request.form
    username = form['Username'].strip().lower()
    print(username)
    wachtwoord = form['Wachtwoord']
    data = (username , wachtwoord)
    print(data)
    try:
        cursor.execute(INSERT_SQL, data)
    except: return "username already exists,niet perse though. Te nemen met een korrel zout"
    connection.commit()
    session["myName"] = request.form["name"]
    return redirect("/login") 

@app.route("/processLogin" , methods = ['POST'])

def processLogin():
    connection,cursor = connect_to_database()
    form = request.form
    username = form['un'].strip().lower()
    wachtwoord = form['pw']
    
    try: 
        viewhashSQL = f"SELECT pw FROM Users where user = '{username}'"
        cursor.execute(viewhashSQL)
        uData = cursor.fetchone()
        session["myName"] = request.form["un"]
        print(session['myName'])
        if wachtwoord == uData[0]:
            session["myName"] = request.form["un"]
            return redirect("/welcome")
        else: return redirect("/gtfo")
    except:
        return("Username prolly not found")

@app.route("/welcome")
def welcome():
    f = open("85_login_Html\welcome.html" , 'r' , encoding= "utf-8")
    page = f.read()
    f.close()
    if session.get("myName"):
        print('sessionfound')
        myName = session["myName"]
        page += f"<h1> welcome {myName}</h1>"
        return page
    else: return "Not logged in"
@app.route("/gtfo")
def gtfo():
    f = open("85_login_Html\gtfo.html" , 'r' , encoding= "utf-8")
    page = f.read()
    f.close()
    return page
@app.route("/login")
def login():
    f = open("85_login_Html\login.html" , 'r' , encoding= "utf-8")
    page = f.read()
    f.close()

    return page

@app.route("/reset")
def reset():
    session.clear()
    return redirect('/')  
    




app.run(host = '0.0.0.0', port = 81)