from flask import Flask, request, redirect, session
import os
import dotenv

#env
dotenv_path = ".devcontainer/devcontainer.env"
dotenv.load_dotenv(dotenv_path)
#app
app = Flask(__name__)
app.secret_key = os.environ['sessionKey']
#stuff
@app.route('/')
def index():
    page = ""
    myName = ''
    if session.get("myName"):
        myName = session["myName"]
    page += f"<h1>{myName}</h1>"
    f = open("form.html" , 'r')
    page = f.read()
    f.close()
    return page
@app.route('/push' , methods=["POST"])
def setName():
    session["myName"] = request.form["name"]
    return redirect("/")

app.run(host = '0.0.0.0' , port = 81)


