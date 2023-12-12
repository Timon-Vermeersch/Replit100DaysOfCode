#https://www.youtube.com/watch?v=g5JOQvR8xUE
##for future: sqlite3 MyFirstDatabase.db "CREATE TABLE diary (date TEXT PRIMARY KEY, entry TEXT NOT NULL);"
from flask import Flask, request, redirect,flash,render_template
import sqlite3 as sq

TABLE_NAME = "Users"
SELECT_SQL = f"SELECT * FROM {TABLE_NAME}"
INSERT_SQL = f"""INSERT INTO {TABLE_NAME}(user, pw)
                 VALUES(?, ?)"""


local_db_path = "84_login_Html\dag84.db"

def connect_to_database():
    connection = sq.connect(local_db_path)
    cursor = connection.cursor()
    return connection, cursor


app = Flask(__name__,template_folder='templates')
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SESSION_PROTECTION'] = 'strong'
@app.route("/" , methods = ['GET'])

def index():
    f = open("84_login_Html\greeting.html" , 'r' , encoding = "utf-8")
    page = f.read()
    f.close
    return page

@app.route("/signup")
def signup():
    f = open("84_login_Html\signup.html" , 'r' , encoding= "utf-8")
    page = f.read()
    f.close
    return page

@app.route("/test")
def trail():
    return render_template(r"84_login_Html\templates\example.html")

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
        if wachtwoord == uData[0]:
            return redirect("/welcome")
        else: return redirect("/gtfo")
    except:
        return("Username prolly not found")
    
    
    



    data = username + wachtwoord
    
    return f"Welcome {username}"
@app.route("/welcome")
def welcome():
    f = open("84_login_Html\welcome.html" , 'r' , encoding= "utf-8")
    page = f.read()
    f.close()
    return page
@app.route("/gtfo")
def gtfo():
    f = open("84_login_Html\gtfo.html" , 'r' , encoding= "utf-8")
    page = f.read()
    f.close()
    return page
@app.route("/login")
def login():
    f = open("84_login_Html\login.html" , 'r' , encoding= "utf-8")
    page = f.read()
    f.close()

    return page

    
    




app.run(host = '0.0.0.0', port = 81)