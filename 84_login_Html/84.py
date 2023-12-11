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


app = Flask(__name__)
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
    username = form['Username'] 
    print(username)
    wachtwoord = form['Wachtwoord']
    data = (username , wachtwoord)
    print(data)
    try:
        cursor.execute(INSERT_SQL, data)
    except: return "username already exists,niet perse though.nemen met een korrel zout"
    connection.commit()
    
    #flash('Thank you for registering')
    #return redirect("/test") 

    
    




app.run(host = '0.0.0.0', port = 81)