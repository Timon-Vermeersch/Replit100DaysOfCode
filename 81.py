from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/process' , methods = ['POST'])

def process():
    robot = "You are a robby botto"
    page = ""
    form = request.form
    if form["youRobot?"] == "on":
        page += robot
    elif form["youRobot?"] == None:
        pass
    elif form["favFood"] == "sf":
        page += robot
    elif "error" in form["inf?"]:
        page += robot
    else:
        page += "welcome human"
    
    #return page
    return request.form

@app.route('/')
def index():
    f = open("81.html" , 'r' , encoding= "utf-8")
    page = f.read()
    f.close
    return page

app.run(host = '0.0.0.0', port=81)