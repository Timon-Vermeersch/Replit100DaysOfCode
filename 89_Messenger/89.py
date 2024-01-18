#https://www.youtube.com/watch?v=gTe4kHcFZJk&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=158

from flask import Flask, request, redirect, session
import os,dotenv,datetime
import sqlite3 as sq



TABLE_NAME_USER = "Users"
SELECT_SQL_USER = f"SELECT * FROM {TABLE_NAME_USER}"
INSERT_SQL_USER = f"""INSERT INTO {TABLE_NAME_USER}(username, password)
                 VALUES(?, ?)"""


TABLE_NAME = "Messages"
SELECT_SQL = f"SELECT * FROM {TABLE_NAME}"
INSERT_SQL = f"""INSERT INTO {TABLE_NAME}(number, message, author, time)
                 VALUES(?, ?, ?, ?)"""

local_db_path = r"89_Messenger\Messenger.db"
dotenv_path = ".devcontainer/devcontainer.env"
dotenv.load_dotenv(dotenv_path)

def connect_to_database():
    connection = sq.connect(local_db_path)
    cursor = connection.cursor()
    return connection, cursor

app = Flask(__name__)
app.secret_key = os.environ['sessionKey']

@app.route("/")
def index():
    connection, cursor = connect_to_database()
    f = open("89_Messenger/chat.html" , 'r' , encoding= 'utf-8')
    page = f.read()
    f.close()

    cursor.execute(f"SELECT number, message, author, time FROM {TABLE_NAME};")
    count_result = cursor.fetchall()
    messages_html = ''
    for thing in reversed(count_result):
        messages_html += f"""<div class="message">
                <span>{thing[0]}|{thing[3]}|-> {thing[2]}:<span class="message-text"> {thing[1]}</span></span>
             
            </div>"""    
    
    page = page.replace('{messageBlock}' , messages_html)
    if session.get("myName"):
        page = page.replace('{guest}' , session['myName'])
    return page
@app.route(r"/login")
def login():
    f = open(r"89_Messenger\login.html" , 'r')
    page = f.read()
    f.close
    return page
@app.route("/processLogin" , methods = ['POST'])
def processLogin():
    connection, cursor = connect_to_database()
    form = request.form
    password = form['password']
    username = form['username']
    print(username,password,"usernamepassword")
    try:
        viewhashSQL = f"SELECT password FROM Users where username = '{username}'"
        cursor.execute(viewhashSQL)
        uData = cursor.fetchone()
        session["myName"] = request.form["username"]
        print(uData,"printuData")
        if password == uData[0]:
            session["myName"] = request.form["username"]
            return redirect('/')
        else: return 'gtfo'
    except:
        return('username prolly not found')
@app.route("/send" , methods = ['POST'])
def sendMessage():
    print("Send Message Endpoint Hit")
    connection , cursor = connect_to_database()

    if session.get("myName"):
        cursor.execute("SELECT number FROM Messages ORDER BY rowid DESC LIMIT 1")
        form = request.form
        print("Form Data:", form)
        message_content = form.get('message-input', 'No message sent')
        print("Message Content:", message_content)
        result = cursor.fetchone()
        print(result)
        if result:
             a = int(result[0]) + 1
        else:
            a = 1
        b = form['message-input']
        c = session["myName"]
        time = datetime.datetime.now()
        d = time.strftime("%Y-%m-%d %H:%M:%S")
        data = (a , b , c , d)
        try:
            cursor.execute(INSERT_SQL, data)
            
        except: return "prolly id error"
        connection.commit()
        return redirect('/')
    else: return "Login First"


@app.route("/reset")
def reset():
    session.clear()
    return redirect('/')
app.run(host = '0.0.0.0' , port = 81,debug=True)

