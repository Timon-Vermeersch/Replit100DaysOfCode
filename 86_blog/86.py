from flask import Flask, request, redirect, session
import sqlite3 as sq
import dotenv
import os
import datetime

#-----------------------------------------------------------------------

TABLE_NAME = "Entries"
SELECT_SQL = f"SELECT * FROM {TABLE_NAME}"
INSERT_SQL = f"""INSERT INTO {TABLE_NAME}(title, content, date, author)
                 VALUES(?, ?, ?, ?)"""

TABLE_NAME_USER = "Users"
SELECT_SQL_USER = f"SELECT * FROM {TABLE_NAME_USER}"
INSERT_SQL_USER = f"""INSERT INTO {TABLE_NAME_USER}(user, password)
                 VALUES(?, ?)"""

local_db_path = r"86_blog\blog.db"
dotenv_path = ".devcontainer/devcontainer.env"
dotenv.load_dotenv(dotenv_path)

def connect_to_database():
    connection = sq.connect(local_db_path)
    cursor = connection.cursor()
    return connection, cursor
#-----------------------------------------------------------------------
app = Flask(__name__)
app.secret_key = os.environ['sessionKey']
#-----------------------------------------------------------------------
@app.route("/")
def index():
    connection , cursor = connect_to_database()
    f = open(r"86_blog\blog.html", 'r')
    page = f.read()
    f.close()
    
        
    cursor.execute(f"SELECT title, content, date, author FROM {TABLE_NAME};")
    count_result = cursor.fetchall()
    articles_html = ''
    for thing in reversed(count_result):
        articles_html += f"""<article>
            <h2>{thing[0]}</h2>
            <p>{thing[1]}</p>
            <p>Posted on {thing[2]} by <a href="#">{thing[3]}</a></p>
        </article>"""
    
    page = page.replace('{articles}' , articles_html)
    if session.get("myName"):
        page = page.replace('{guest}' , session['myName'])
    

    return page
@app.route(r"/login")
def login():
    f = open(r"86_blog\login.html", 'r')
    page = f.read()
    f.close()
    return page
@app.route("/processLogin" , methods = ['POST'])
def processLogin():
    connection , cursor = connect_to_database()
    form = request.form
    password = form['password']
    username = form['username']
    print(username,password)
    try:
        viewhashSQL = f"SELECT password FROM Users where user = '{username}'"
        cursor.execute(viewhashSQL)
        uData = cursor.fetchone()
        session["myName"] = request.form["username"]
        print(uData)
        if password == uData[0]:
                session["myName"] = request.form["username"]
                return redirect('/')
        else: return 'gtfo'
    except:
        return("username prolly not found")
@app.route("/submit" , methods = ['POST'])
def submitPost():
    connection , cursor = connect_to_database()
    if session.get("myName"):
        form = request.form
        a = form['content']
        b = form['title']
        c = session["myName"]
        d = datetime.datetime.now()
        year = d.year
        month = d.month
        day = d.day
        hour = d.hour
        minute = d.minute
        second = d.second
        microsecond = d.microsecond
        formatted_date = d.strftime("%Y-%m-%d %H:%M:%S")
        data = (b,a,formatted_date,c)
        try:
            cursor.execute(INSERT_SQL, data)
        except: return "title already exists,niet perse though. Te nemen met een korrel zout"
        connection.commit()
        
        return redirect('/')
    else: return'Login first'

@app.route("/reset")
def reset():
    session.clear()
    return redirect('/') 

    










app.run(host = '0.0.0.0', port = 3001)
