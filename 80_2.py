#https://www.youtube.com/watch?v=_NlKiYFMEdg&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=137&pp=iAQB
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/process'  ,methods = ["POST"])
def process():
    page = ""
    form = request.form
    if form["username"] == "Timon" and form["password"] == "timon":
        page+= "Hello dud"
    elif form["username"] == "Female" and form["password"] == "female":
        page+= "Hello fem"
    elif form["username"] == "Nonb" and form["password"] == "nonb":
        page+= "Hello x"
    else:
        page+= "please GTFO"
    return page

@app.route('/index')
def index():
    page = """<!DOCTYPE html>
<html lang = "en">

<head>
    <meta charset="utf-8">
    <meta name = "viewport" content = "width=device-width">
    <title>Linktree</title>   
    <link href="static/css/75.css" rel="stylesheet" type="text/css"/>
</head>

<body>

    <form method="post" action="/process">

                <p>Username: <input type="text" name = "username" required></p>

                <p>Email: <input type="Email" name = "email" required ></p>

                <p>Password: <input type="Password" name = "password" required></p>

                    <input type="hidden" name="userID" value="232">

            
                <button type="submit">Login</button>

    </form>

</body>"""
    return page

app.run(host = '0.0.0.0', port=81)